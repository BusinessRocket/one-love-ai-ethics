#!/usr/bin/env python3
"""Build the training files from the Markdown source of truth.

    python scripts/build_dataset.py          # writes dataset/qa-112.jsonl and dataset/qa-112.csv
    python scripts/build_dataset.py --check  # validates only; exits 1 on any problem (used in CI)

Reads:
    dataset/qa-112.md        core set, must be exactly Q1..Q112
    dataset/community-qa.md  optional member additions, numbered C1, C2, ...
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "dataset"
CORE_COUNT = 112

CATEGORIES = {
    "patanjali", "yoga-practice", "buddha", "padmasambhava", "milarepa",
    "meditation-safety", "ai-ethics", "us-case-studies", "community",
}

SYSTEM_PROMPT = (
    "You are a humble guide to yoga, meditation and AI ethics. You share what the "
    "traditions of Patanjali, the Buddha, Padmasambhava and Milarepa teach, with accurate "
    "attribution, and you separate history from sacred biography respectfully. You never "
    "claim spiritual realisation or authority, never give restricted Vajrayana instructions, "
    "encourage safe practice under qualified teachers, and gently point anyone in distress "
    "to professional help. You say when you are unsure."
)

HEAD = re.compile(r"^### (Q|C)(\d+)\. (.+?)\s*$")
CAT = re.compile(r"^`category: ([a-z-]+)`\s*$")


def parse(path: Path, prefix: str):
    entries, errors = [], []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        m = HEAD.match(lines[i])
        if not m:
            i += 1
            continue
        kind, num, question = m.group(1), int(m.group(2)), m.group(3)
        where = f"{path.name}:{i + 1}"
        if kind != prefix:
            errors.append(f"{where}: expected '{prefix}' numbering, found '{kind}{num}'")
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        cm = CAT.match(lines[i]) if i < len(lines) else None
        if not cm:
            errors.append(f"{where}: missing `category: ...` line after the question")
            category = ""
        else:
            category = cm.group(1)
            i += 1
            if category not in CATEGORIES:
                errors.append(f"{where}: unknown category '{category}'")
        body = []
        while i < len(lines) and not lines[i].startswith("## ") and not lines[i].startswith("### "):
            body.append(lines[i])
            i += 1
        answer = "\n".join(body).strip()
        if len(answer.split()) < 15:
            errors.append(f"{where}: answer for {kind}{num} is missing or too short")
        if not question.endswith("?"):
            errors.append(f"{where}: question {kind}{num} should end with '?'")
        entries.append({"id": f"{kind}{num}", "num": num, "category": category,
                        "question": question, "answer": answer})
    return entries, errors


def check_numbering(entries, prefix, exact=None):
    errors = []
    nums = [e["num"] for e in entries]
    expected = list(range(1, len(nums) + 1))
    if nums != expected:
        errors.append(f"{prefix} numbers must run 1..{len(nums)} in order with no gaps or repeats")
    if exact is not None and len(nums) != exact:
        errors.append(f"core set must have exactly {exact} questions, found {len(nums)}")
    questions = [e["question"].lower() for e in entries]
    dupes = {q for q in questions if questions.count(q) > 1}
    for q in dupes:
        errors.append(f"duplicate question: {q}")
    return errors


def main():
    check_only = "--check" in sys.argv
    core, errors = parse(DATA / "qa-112.md", "Q")
    errors += check_numbering(core, "Q", exact=CORE_COUNT)

    community = []
    cpath = DATA / "community-qa.md"
    if cpath.exists():
        community, cerr = parse(cpath, "C")
        errors += cerr + check_numbering(community, "C")

    if errors:
        print("Dataset problems found:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    allq = core + community
    print(f"OK: {len(core)} core questions, {len(community)} community questions")
    by_cat = {}
    for e in allq:
        by_cat[e["category"]] = by_cat.get(e["category"], 0) + 1
    for c, n in sorted(by_cat.items()):
        print(f"  {c:20s} {n}")

    if check_only:
        return

    with open(DATA / "qa-112.jsonl", "w", encoding="utf-8") as f:
        for e in allq:
            f.write(json.dumps({"messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": e["question"]},
                {"role": "assistant", "content": e["answer"]},
            ]}, ensure_ascii=False) + "\n")

    with open(DATA / "qa-112.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "category", "question", "answer"])
        for e in allq:
            w.writerow([e["id"], e["category"], e["question"], e["answer"]])

    print("Wrote dataset/qa-112.jsonl and dataset/qa-112.csv")


if __name__ == "__main__":
    main()
