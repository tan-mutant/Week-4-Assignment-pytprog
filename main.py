from audit_tool import clean_transactions, apply_service_fee, calculate_nested_total


def main():
    raw = [250.0, -40.0, 0, 8.5, 10.0, 75.25, 9.99, 1200.0, -3.0, 15.5]
    print("=== Task 1: Cleaning and Fees ===")
    print("Raw batch        :", raw)
    cleaned = clean_transactions(raw)
    print("Cleaned (min 10) :", cleaned)
    print("Cleaned (min 50) :", clean_transactions(raw, min_threshold=50.0))
    print("After 2% fee     :", apply_service_fee(cleaned))
    print("After 5% fee     :", apply_service_fee(cleaned, fee_rate=0.05))

    print("\n=== Task 2: Recursive Nested Total ===")
    tests = [
        ("Empty list", []),
        ("Single int", 100),
        ("Single float", 49.75),
        ("Flat list", [10, 20, 30]),
        ("Assignment example", [100, [50, 25], [[10, 5], 40]]),
        ("Deep nesting", [1, [2, [3, [4, [5.5]]]]]),
        ("Empty sublists", [[], [5, []], [[], [[], 7]]]),
    ]
    for label, data in tests:
        print(f"{label:<20}{str(data):<38}-> {calculate_nested_total(data)}")

    print("\n=== Audit pipeline on a nested batch ===")
    batch = [[250.0, -40.0, 8.5], [[1200.0, 15.5], [9.99, 75.25]], 10.0]
    gross = calculate_nested_total(batch)
    print("Nested batch     :", batch)
    print("Gross total      :", gross)
    print("Net after 2% fee :", apply_service_fee([gross])[0])


if __name__ == "__main__":
    main()
