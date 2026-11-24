import os

LINE = "v32.4: Fixed a bug where entering a room caused memory leak and immediate loss of primary objective. Coffee buff duration reduced by 40%."

def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
