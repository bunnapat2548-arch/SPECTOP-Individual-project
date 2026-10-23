# Using GenAI to Analyze Central Bank Communication

University assignment (Module 6: Press Conference vs Written Statement). It compares the FOMC policy statement of **September 16, 2026** with Chair Warsh's press conference that day, to see whether the press conference gave information beyond the statement.

The analysis was done with **Claude Code**, so every input and output is a plain-text or Markdown file.

| Path | What it is |
|---|---|
| `CLAUDE.md` | Instructions given to the AI tool (role, evidence rules, definitions, output format) |
| `statement.md` | FOMC statement, verbatim from federalreserve.gov |
| `transcript.md` | Word-for-word text of the press conference transcript, with page markers |
| `Sources/` | Original transcript PDF and saved statement web page |
| `outputs/prompt1.md` – `prompt7.md` | Each prompt as typed, followed by the tool's full answer |
| `outputs/prompt7_readability.py` | Python script for word counts and Flesch-Kincaid grade (`python outputs/prompt7_readability.py`) |
