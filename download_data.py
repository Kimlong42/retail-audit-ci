import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"
DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "online_retail_II.csv"


def main() -> None:
    if CSV_PATH.exists():
        print("Data đã có, bỏ qua download.")
        return
    DATA_DIR.mkdir(exist_ok=True)
    zip_path = DATA_DIR / "raw.zip"
    urllib.request.urlretrieve(URL, zip_path)
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(DATA_DIR)
    xlsx = next(DATA_DIR.glob("*.xlsx"))
    df = pd.concat(pd.read_excel(xlsx, sheet_name=None).values())
    df.to_csv(CSV_PATH, index=False)
    print(f"Đã lưu {len(df):,} dòng vào {CSV_PATH}")


if __name__ == "__main__":
    main()
