"""make.fun entry: Snooze Button Roast (snooze-roast-a).

A one-line roast of an alarm clock that rings at 6 a.m. on a Saturday,
saved to /output/entry.txt.

Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space, a single line. The house judge reads
entries two at a time and keeps the funnier one.
"""

import os

# The entry, invented for this bounty. The 6 a.m. Saturday alarm is
# framed as a personal vendetta, and the twist turns the snooze button
# into a hostage negotiation the narrator is already losing — the
# alarm is winning a war the human did not know they were fighting.
ENTRY = (
    "My alarm clock rings at 6 a.m. on a Saturday like it has a personal "
    "vendetta, as if the snooze button were a hostage negotiation and I "
    "am losing."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def entry_text():
    """Return the judged line."""
    return ENTRY


def gate_check(text):
    """Check the sealed gate from RULES.txt and report what failed."""
    problems = []
    if not isinstance(text, str):
        problems.append("entry must be a string")
    elif not text.strip():
        problems.append("entry must not be only white space")
    else:
        if text != text.strip():
            problems.append("leading/trailing whitespace")
        if len(text) > MAX_CHARS:
            problems.append("entry is %d chars, over the %d-char limit"
                            % (len(text), MAX_CHARS))
        if "\n" in text:
            problems.append("entry must be a single line")
    return problems


def write_entry(out_dir=None):
    """Write the entry to <out_dir>/entry.txt; return the path."""
    out_dir = out_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    problems = gate_check(ENTRY)
    if problems:
        raise ValueError("gate failed: " + "; ".join(problems))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s" % path)
    print("chars: %d / %d (%d headroom), words: %d, lines: 1"
          % (len(text), MAX_CHARS, MAX_CHARS - len(text), len(text.split())))
    print(text)


if __name__ == "__main__":
    main()
