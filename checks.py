from pathlib import Path

import pandas as pd

CSV_PATH = Path("data/online_retail_II.csv")


def load_raw() -> pd.DataFrame:
    return pd.read_csv(CSV_PATH, dtype={"Invoice": str, "StockCode": str})


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df[~df["Invoice"].str.startswith("C")]  # loại hóa đơn hủy
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]  # loại điều chỉnh/lỗi
    return df
