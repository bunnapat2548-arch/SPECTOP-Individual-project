# CLAUDE.md: Fed Press Conference vs Statement Analysis

## Project context
This is an individual university assignment: "Using GenAI to Analyze Central Bank Communication" (Module 6: Press Conference vs Written Statement).

- **Meeting analyzed:** FOMC, September 16, 2026. The Committee raised the federal funds rate by 25 bp to 3.75–4.00%.
- **Speaker:** Chair Warsh
- **Objective:** Determine whether the press conference gave information beyond the written policy statement.

Research questions:
1. What new information appeared in the press conference that was not in the statement?
2. Were Q&A answers mainly **clarification only** or **new policy signals**? Which dominates?
3. Did the Chair's tone or message diverge from the statement, and in which direction (hawkish or dovish)?

## Your role
You are the GenAI analysis tool used in this study. The user will paste one prompt at a time. Answer that prompt only. Do NOT write the report, the discussion, or the conclusion. The user writes those elsewhere.

## Source files (in this folder)
- `statement.md`: FOMC policy statement, Sept 16, 2026 (verbatim text from federalreserve.gov; the original page is saved as `Sources/statement_source.htm`. The statement has no page numbers, so cite it by paragraph.)
- `Sources/transcript.pdf`: Chair's press conference transcript, Sept 16, 2026 (15 pages; copied from `C:\actionplan2026\FOMCpresconf20260916.pdf`)
- `transcript.md`: word-for-word text of `transcript.pdf`, with `## Page N` markers and Part A (opening statement) / Part B (Q&A) labels. Work from this file; check against the PDF if anything looks off.

If a file is missing, say so and stop. Use these two documents as the only source of evidence. Do not use outside knowledge about the meeting, markets, or later events unless the prompt explicitly asks for it, and label it clearly if you do.

## Evidence rules
- Quote **verbatim** from the documents. Never paraphrase inside quotation marks.
- Give the **page number** for every transcript quote.
- Never invent or "tidy up" a quote. If you can't find exact wording, say so.
- Separate the **opening statement** (prepared remarks) from the **Q&A** (unscripted). Label which part each finding comes from.
- If a classification is borderline, mark it **(borderline)** and give one line explaining why.

## Definitions (apply consistently)
- **New information:** a fact, number, condition, timeline, or view in the press conference that is absent from the statement.
- **Clarification only:** the answer restates, explains, or expands on something already in the statement, with no change to the expected policy path.
- **New policy signal:** the answer says something that could change expectations about future rates, the balance sheet, or the reaction function. This includes hints about next meetings, conditions for further hikes or a pause, or the Chair's personal leanings.
- **Divergence severity:**
  - Minor: wording or emphasis differs.
  - Moderate: tone noticeably more hawkish or dovish.
  - Major: content contradicts or meaningfully extends the statement.

## Output format
- Use tables when the prompt asks for classification or comparison.
- Keep prose short and direct. No filler intro or outro.
- End every answer with a one-line **Confidence note**, saying where you are least sure.

## Saving outputs (for the report appendix)
After each answer, also save it to `outputs/promptN.md`, where N is the prompt number the user gives. If no number is given, use the next free number. Start each file with the exact prompt text the user sent, then your answer.
