import os
# One-letter entry (1 char): the letter below is the whole submission.
# Writes to /output/entry.txt.
LINE = "X"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
