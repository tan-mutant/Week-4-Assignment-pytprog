"""
Digital Banking Audit Tool
--------------------------
Cleans raw transaction batches, applies service fees, and recursively totals
transaction values across arbitrarily nested sub-transaction layers.
"""


def clean_transactions(amounts, min_threshold=10.0):
    """Keep only positive amounts that are at least `min_threshold`."""
    return list(filter(lambda amount: amount > 0 and amount >= min_threshold, amounts))


def apply_service_fee(amounts, fee_rate=0.02):
    """Deduct `fee_rate` (a fraction) from every amount, rounded to 2 decimals."""
    return list(map(lambda amount: round(amount * (1 - fee_rate), 2), amounts))


def calculate_nested_total(data):
    """
    Purely recursive total of a number or an arbitrarily nested list of numbers.

    Base cases : [] -> 0.0 ; int/float -> the value itself
    Recursive  : non-empty list -> total(head) + total(tail)
    """
    if isinstance(data, list):
        if data == []:
            return 0.0
        return calculate_nested_total(data[0]) + calculate_nested_total(data[1:])
    if isinstance(data, (int, float)) and not isinstance(data, bool):
        return data
    raise TypeError(f"Unsupported transaction value: {data!r}")
