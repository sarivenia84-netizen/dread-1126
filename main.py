import os
import pathlib

OUTPUT_DIR = pathlib.Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
FALLBACK_DIR = pathlib.Path("./output")
FALLBACK_FILE = FALLBACK_DIR / "entry.txt"

review_comment = "Approve: clean error handling removes noise, yet uneasy knowing today's fix will one day confuse inherited cruft without a map."

def main():
    out = OUTPUT_FILE if OUTPUT_DIR.exists() else FALLBACK_FILE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(review_comment)

if __name__ == "__main__":
    main()