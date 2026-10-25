# One Love AI Ethics 🙏

**Yoga, meditation and responsible AI — an open dataset and a circle of practitioners.**

An open-source project that gathers the wisdom of **Patanjali**, the **Buddha**, **Padmasambhava (Guru Rinpoche)** and **Milarepa** into 112 carefully written questions and answers, connects it to today's real **AI ethics cases in the United States**, and invites anyone, anywhere, to join and contribute — so we can share one love and peace toward our true home: self-realisation.

> Why 112? In the *Vijñāna Bhairava Tantra*, Shiva offers Devi 112 ways of meditation — 112 doors into the same awareness. This dataset offers 112 questions as doors into practice and into responsible technology.

---

## What's inside

| Path | What it is |
|---|---|
| [`dataset/qa-112.md`](dataset/qa-112.md) | **The 112 questions and answers** — readable, editable source of truth |
| [`dataset/qa-112.jsonl`](dataset/qa-112.jsonl) | The same 112 in chat format for fine-tuning or evaluating an AI |
| [`dataset/qa-112.csv`](dataset/qa-112.csv) | The same 112 for spreadsheets |
| [`dataset/README.md`](dataset/README.md) | Dataset card: format, intended use, limits |
| [`docs/meditation-dos-and-avoids.md`](docs/meditation-dos-and-avoids.md) | **Survey of meditation dos and avoids** across all four teachers, plus modern safety research and a member self-check |
| [`docs/us-ai-case-studies-2026.md`](docs/us-ai-case-studies-2026.md) | **Ten current U.S. AI case studies** (2025–2026), each read through a contemplative lens |
| [`ETHICS.md`](ETHICS.md) | **The One Love AI Ethics Charter** — 12 principles from the yamas, niyamas and the Buddha's path |
| [`MEMBERS.md`](MEMBERS.md) | **The circle** — add your name to connect with other members |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to join, add questions and fix mistakes |

### The 112 questions

| Part | Topic | Questions |
|---|---|---|
| 1 | Patanjali & the Yoga Sutras | Q1–Q20 |
| 2 | Yoga practice & safety | Q21–Q30 |
| 3 | The Buddha & Buddhist meditation | Q31–Q46 |
| 4 | Padmasambhava & Vajrayana | Q47–Q56 |
| 5 | Milarepa & the Kagyu lineage | Q57–Q66 |
| 6 | Meditation dos & avoids | Q67–Q82 |
| 7 | AI ethics through a contemplative lens | Q83–Q102 |
| 8 | U.S. AI case studies 2025–2026 | Q103–Q112 |

---

## Join the circle — connect with other members

1. ⭐ **Star** and **Watch** this repository to follow new contributions.
2. 🙋 **Introduce yourself**: open an issue with the **"Join the circle"** form, or add a line to [`MEMBERS.md`](MEMBERS.md) through a pull request.
3. 💬 **Talk with members** in **Discussions** (the *Discussions* tab): share practice, ask questions, plan online sits.
4. 📝 **Answer the practice survey** with the **"Practice survey"** issue form.
5. 🪷 **Contribute**: suggest a question, correct a fact, translate (Dzongkha, Hindi, Nepali, Tibetan and more are especially welcome). See [`CONTRIBUTING.md`](CONTRIBUTING.md).

No experience with GitHub needed — the issue forms work from any browser, including on a phone.

---

## Using the dataset to train or test an AI

```bash
python scripts/build_dataset.py          # rebuild jsonl + csv from the Markdown source
python scripts/build_dataset.py --check  # validate only (also runs automatically on every pull request)
```

Each line of `qa-112.jsonl` is one conversation in the common `messages` format (system, user, assistant), compatible with most chat fine-tuning tools.

**Please train responsibly** (see [`dataset/README.md`](dataset/README.md)):
- 112 examples are enough to **shape tone and values**, not to teach deep knowledge. Use it as a style/values set or an **evaluation set**.
- Keep the humble system prompt. A model trained on this must **never** present itself as a guru or enlightened being.
- Have practitioners review outputs, and test for invented quotes and unsafe advice.

---

## Principles in one breath

Ethics first. Truth always. Harm prevented before it arises. Lineages honoured. No AI gurus. Safety over mystique. One love.

---

## Important notes

- **Not medical or psychological advice.** Meditation and breathwork can be difficult for some people. If you are struggling, contact a health professional or a crisis line — Lifeline **13 11 14** (Australia), **988** (United States).
- **Not a substitute for a teacher.** Where a tradition says a practice requires empowerment or transmission, this project describes it but does not teach it.
- **History and sacred biography.** Stories of Padmasambhava and Milarepa are presented as tradition tells them, with historical notes where useful, and with respect for both.
- **Case studies are current to October 2026** and may change. Corrections are welcome.
- **Made with AI help.** The first draft was written with Claude (made by Anthropic) and is meant to be reviewed and improved by human practitioners.

## License

- Text and dataset (`dataset/`, `docs/`, `ETHICS.md`, this README): [Creative Commons Attribution 4.0](LICENSE-CONTENT.md) — share and adapt freely with credit.
- Code (`scripts/`, `.github/`): [MIT](LICENSE).

*Sarva maṅgalam — may all be auspicious.* 🌏
