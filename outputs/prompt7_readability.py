"""Prompt 7: word counts and Flesch-Kincaid grade level.

Parts measured:
  1. Statement        - the three policy paragraphs in statement.md
                        (header, source note, release time and vote preamble excluded)
  2. Opening statement - Part A of transcript.md, speaker label removed
  3. Q&A answers       - every CHAIRMAN WARSH turn in Part B of transcript.md
                        (reporters and moderator excluded), speaker label removed

Flesch-Kincaid grade = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

Standard library only. Usage (from the project folder):
    python outputs/prompt7_readability.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEAKER = re.compile(r"^((?:[A-Z][A-Z’'\-]+ ){1,3}[A-Z][A-Z’'\-]+)\. ")

# Abbreviations whose period does not end a sentence
ABBREVIATIONS = ["U.S.", "Mr.", "Mrs.", "Ms.", "Dr.", "p.m.", "a.m.", "e.g.", "i.e."]


def statement_text():
    lines = (ROOT / "statement.md").read_text(encoding="utf-8").split("\n")
    body = lines[lines.index("---") + 1:]
    keep = [l for l in body if l.strip()
            and not l.startswith("For release")
            and not l.startswith("The Federal Open Market Committee approved")]
    return keep


def transcript_parts():
    text = (ROOT / "transcript.md").read_text(encoding="utf-8")
    part_a = text.split("### Part A")[1].split("### Part B")[0]
    part_b = text.split("### Part B")[1]

    def paragraphs(block):
        return [l.strip() for l in block.split("\n")
                if l.strip() and not l.startswith("#")]

    opening = [SPEAKER.sub("", p) for p in paragraphs(part_a)]

    answers, speaker = [], None
    for p in paragraphs(part_b):
        m = SPEAKER.match(p)
        if m:
            speaker = m.group(1)
            p = p[m.end():]
        if speaker == "CHAIRMAN WARSH":
            answers.append(p)
    return opening, answers


def sentences(text):
    t = text
    for abbr in ABBREVIATIONS:
        t = t.replace(abbr, abbr.replace(".", "<DOT>"))
    t = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)          # decimals such as 4.1
    parts = re.split(r"(?<=[.!?])[”\"’)]*\s+", t.strip())
    return [s for s in parts if re.search(r"[A-Za-z0-9]", s)]


def words(text):
    # Em/en dashes join words in the transcript ("jobless—the"); split on them
    tokens = re.split(r"[\s—–]+", text)
    return [w for w in tokens if re.search(r"[A-Za-z0-9¼½¾]", w)]


def syllables(word):
    w = word.lower()
    w = re.sub(r"[’']s$", "", w)
    letters = re.sub(r"[^a-z]", "", w)
    if not letters:            # pure numbers such as 3.6 or ¼: count as one syllable
        return 1
    groups = re.findall(r"[aeiouy]+", letters)
    n = len(groups)
    if letters.endswith("e") and not letters.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1                 # silent final e (rate, decide)
    if letters.endswith("ed") and not letters.endswith(("ted", "ded")) and n > 1:
        n -= 1                 # silent -ed (raised, noted is kept)
    return max(n, 1)


def measure(name, paragraphs):
    text = " ".join(paragraphs)
    ws = words(text)
    ss = sentences(text)
    syl = sum(syllables(w) for w in ws)
    wps = len(ws) / len(ss)
    spw = syl / len(ws)
    fk = 0.39 * wps + 11.8 * spw - 15.59
    return {"part": name, "paragraphs": len(paragraphs), "words": len(ws),
            "sentences": len(ss), "syllables": syl,
            "words_per_sentence": wps, "syllables_per_word": spw, "fk_grade": fk}


def main():
    opening, answers = transcript_parts()
    rows = [measure("Statement", statement_text()),
            measure("Opening statement", opening),
            measure("Q&A answers (Chair only)", answers)]
    hdr = ("Part", "Words", "Sentences", "Syllables", "Words/sent", "Syll/word", "FK grade")
    print("| " + " | ".join(hdr) + " |")
    print("|" + "---|" * len(hdr))
    for r in rows:
        print(f"| {r['part']} | {r['words']} | {r['sentences']} | "
              f"{r['syllables']} | {r['words_per_sentence']:.1f} | "
              f"{r['syllables_per_word']:.2f} | {r['fk_grade']:.1f} |")
    if "--dump" in sys.argv:   # print the exact text measured, for checking
        for name, paras in [("STATEMENT", statement_text()), ("OPENING", opening), ("QA", answers)]:
            print(f"\n=== {name} ===")
            for p in paras:
                print(p)


if __name__ == "__main__":
    main()
