# Contributing — joining the circle

Everyone is welcome: practitioners of any tradition or none, students, developers, researchers, teachers, translators. You do not need to know how to code.

## Ways to take part

| I want to… | Do this |
|---|---|
| Say hello and connect | Open an issue → **Join the circle**, or add yourself to `MEMBERS.md` |
| Talk, ask, share practice | Go to the **Discussions** tab |
| Share my practice experience | Open an issue → **Practice survey** |
| Suggest a new question | Open an issue → **Propose a question**, or edit `dataset/community-qa.md` |
| Fix a mistake | Open an issue → **Correction**, or edit the file directly |
| Translate | Open a Discussion in *Translations* first so we can coordinate |

## Adding yourself to MEMBERS.md (from a phone or browser)

1. Open `MEMBERS.md` and tap the ✏️ pencil icon.
2. Add one line at the bottom of the table (format shown in the file).
3. Tap **Commit changes** → **Propose changes** → **Create pull request**.

GitHub makes a copy for you automatically. A maintainer will merge it.

## Adding a question

Add it to the bottom of `dataset/community-qa.md`:

```markdown
### C1. Your question here?
`category: community`

Your answer in your own words, at least fifteen words. End with a short source or lineage note, e.g. (Source: Yoga Sutra 2.46).
```

Then run, if you can:

```bash
python scripts/build_dataset.py
```

If you can't run Python, that's fine — the automatic check on your pull request will tell you if anything needs fixing.

## Quality standards

Every contribution should be:

1. **Truthful (satya)** — accurate, with sources for claims about texts, teachers, history, science or law. Mark legend as legend.
2. **Your own words (asteya)** — no copying from copyrighted translations, books, articles or websites. Short quotes from ancient texts are fine; paraphrase modern translations.
3. **Safe (ahiṃsā)** — no instructions for restricted Vajrayana practices, extreme breathwork, fasting or austerities. Include safety notes where relevant.
4. **Respectful** — honour every lineage on its own terms. No ranking of traditions, no mocking beliefs, no selling.
5. **Humble** — no claims of personal realisation, and nothing that presents an AI as a spiritual authority.

## Corrections to the U.S. case studies

Laws and lawsuits change quickly. When something is out of date, include a link to a reliable source (court record, government site, major news outlet or law-firm analysis) and the date.

## Code of conduct

By taking part you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
