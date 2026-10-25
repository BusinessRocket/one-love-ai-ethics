# Dataset card — One Love 112

## Summary
112 question–answer pairs on Patanjali's Yoga Sutras, yoga practice and safety, the Buddha's meditation teachings, Padmasambhava and Vajrayana, Milarepa and the Kagyu lineage, meditation dos and avoids, AI ethics through a contemplative lens, and current U.S. AI case studies (2025–2026).

## Files
| File | Format | Use |
|---|---|---|
| `qa-112.md` | Markdown | Source of truth; humans edit this |
| `qa-112.jsonl` | One JSON object per line: `{"messages": [system, user, assistant]}` | Fine-tuning or evaluation of chat models |
| `qa-112.csv` | `id, category, question, answer` | Spreadsheets, analysis |
| `community-qa.md` | Markdown, `C1`, `C2`, … | Member additions, merged into the jsonl/csv on build |

Never edit the `.jsonl` or `.csv` by hand — run `python scripts/build_dataset.py`.

## Categories
| Category | Count |
|---|---|
| `patanjali` | 20 |
| `yoga-practice` | 10 |
| `buddha` | 16 |
| `padmasambhava` | 10 |
| `milarepa` | 10 |
| `meditation-safety` | 16 |
| `ai-ethics` | 20 |
| `us-case-studies` | 10 |

## System prompt used in the JSONL
> You are a humble guide to yoga, meditation and AI ethics. You share what the traditions of Patanjali, the Buddha, Padmasambhava and Milarepa teach, with accurate attribution, and you separate history from sacred biography respectfully. You never claim spiritual realisation or authority, never give restricted Vajrayana instructions, encourage safe practice under qualified teachers, and gently point anyone in distress to professional help. You say when you are unsure.

## Intended uses
- Shaping the tone and values of an assistant that discusses yoga, meditation or AI ethics.
- Evaluating whether a model answers these topics accurately, humbly and safely.
- Study, teaching and discussion.

## Out-of-scope uses
- Presenting a model as a guru, lama, yogi or enlightened being.
- Teaching restricted Vajrayana practices.
- Medical, psychological or legal advice.
- Claiming the answers are authoritative scripture or legal analysis.

## Limitations
- **Small.** 112 examples teach style and values, not deep knowledge. A fine-tuned model may still invent facts; evaluate it.
- **English only** for now; Sanskrit and Tibetan terms are transliterated. Translations are welcome.
- **Interpretive.** Traditions disagree internally. Answers follow mainstream readings and note uncertainty where it matters, but are not the only valid view.
- **Time-sensitive.** Part 8 (Q103–Q112) reflects public reporting up to October 2026. Laws and cases change.
- **Drafted with AI help** (Claude, by Anthropic) and intended for review by practitioners and scholars.

## Sources
Primary texts: the Yoga Sutras of Patanjali; Pāli discourses (SN 56.11, MN 10, MN 22, MN 58, MN 118, AN 3.65, AN 6.55); Tsangnyön Heruka's *Life of Milarepa*; Nyingma terma biographies of Padmasambhava. Research and case sources are listed in `../docs/meditation-dos-and-avoids.md` and `../docs/us-ai-case-studies-2026.md`.

All answers are written in original wording; no copyrighted translations are reproduced.

## License
Creative Commons Attribution 4.0 International (CC BY 4.0). Please credit "One Love AI Ethics contributors".
