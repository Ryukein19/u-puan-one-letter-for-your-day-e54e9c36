import os
# One-letter entry: the letter below is the whole submission.
LINE = "X"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
