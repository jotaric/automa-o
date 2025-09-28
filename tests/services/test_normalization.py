import math

from app.services.normalization import normalize_product


def test_normalize_product_nan_prices_default_to_zero() -> None:
    raw_product = {"preco_atual": math.nan, "preco_anterior": math.nan}

    normalized = normalize_product(raw_product)

    assert normalized["preco_atual"] == 0.0
    assert normalized["preco_anterior"] == 0.0
