import csv
from pathlib import Path


def detect_line_type(row):
    return row[0]


def parse_report(input_path, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            row = line.strip().split("~")
            line_type = detect_line_type(row)

            if line_type == "01":
                with open(output_dir / "bo_accounts.csv", "w", newline="") as out:
                    writer = csv.writer(out)
                    writer.writerow(["dp_id", "bo_id", "from_date", "to_date"])
                    writer.writerow(row[1:])

            elif line_type == "02":
                with open(output_dir / "isin_master.csv", "a", newline="") as out:
                    writer = csv.writer(out)
                    writer.writerow([row[1], row[2], row[4], row[5]])

            elif line_type == "03" or line_type == "05":
                with open(output_dir / "balances.csv", "a", newline="") as out:
                    writer = csv.writer(out)
                    typ = "opening" if line_type == "03" else "closing"
                    writer.writerow([typ, row[1], row[-1]])

            elif line_type == "04":
                with open(output_dir / "transactions.csv", "a", newline="") as out:
                    writer = csv.writer(out)
                    writer.writerow(row[1:7])
