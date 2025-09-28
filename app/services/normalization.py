"""Utilities for normalizing product data."""
from __future__ import annotations

import math
import re
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Optional


_PRICE_SANITIZER = re.compile(r"[^0-9,.-]")


def _sanitize_price(raw_value: Any) -> Optional[float]:
    """Convert the given value to a float price.

    Parameters
    ----------
    raw_value:
        The value to be sanitized. Strings may contain currency symbols,
        thousand separators or commas. Numbers are returned as floats.

    Returns
    -------
    Optional[float]
        The sanitized price or ``None`` if the value cannot be interpreted as
        a number.
    """

    if raw_value is None:
        return None

    if isinstance(raw_value, bool):  # bool is a subclass of int; treat explicitly.
        return float(raw_value)

    if isinstance(raw_value, str):
        candidate = raw_value.strip()
        if not candidate:
            return None

        candidate = _PRICE_SANITIZER.sub("", candidate)
        # If we have both comma and dot, assume comma is decimal separator as
        # commonly found in pt-BR locales.
        if "," in candidate and "." in candidate:
            candidate = candidate.replace(".", "").replace(",", ".")
        else:
            candidate = candidate.replace(",", ".")

        try:
            value = float(candidate)
        except ValueError:
            return None
        return value

    if isinstance(raw_value, Decimal):
        if raw_value.is_nan():
            return None
        try:
            return float(raw_value)
        except (TypeError, ValueError, InvalidOperation):
            return None

    if isinstance(raw_value, (int, float)):
        if isinstance(raw_value, float) and math.isnan(raw_value):
            return None
        return float(raw_value)

    return None


def normalize_product(raw_product: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a product dictionary.

    The current normalization process focuses on ensuring price fields are
    floats. Missing or invalid price values fall back to ``0.0``.
    """

    normalized: Dict[str, Any] = dict(raw_product)

    for field in ("preco_atual", "preco_anterior"):
        price = _sanitize_price(raw_product.get(field))
        normalized[field] = 0.0 if price is None else price

    return normalized


__all__ = ["normalize_product"]
