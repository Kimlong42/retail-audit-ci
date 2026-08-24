import pytest

from checks import CSV_PATH, clean, load_raw


@pytest.fixture(scope="session")
def raw():
    if not CSV_PATH.exists():
        pytest.fail("Chưa có data — chạy download_data.py trước")
    return load_raw()


@pytest.fixture(scope="session")
def cleaned(raw):
    return clean(raw)


def test_schema(raw):
    expected = {
        "Invoice",
        "StockCode",
        "Quantity",
        "InvoiceDate",
        "Price",
        "Customer ID",
        "Country",
    }
    assert expected <= set(raw.columns)


def test_khong_con_hoa_don_huy(cleaned):
    assert not cleaned["Invoice"].str.startswith("C").any()


def test_gia_va_so_luong_duong(cleaned):
    assert (cleaned["Quantity"] > 0).all()
    assert (cleaned["Price"] > 0).all()


def test_so_dong_hop_ly(cleaned):
    assert len(cleaned) > 5_000_000
