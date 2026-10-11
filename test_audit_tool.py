import unittest
from audit_tool import clean_transactions, apply_service_fee, calculate_nested_total


class TestCleaning(unittest.TestCase):
    def test_removes_non_positive_and_small(self):
        self.assertEqual(clean_transactions([-5, 0, 9.99, 10, 50]), [10, 50])

    def test_custom_threshold(self):
        self.assertEqual(clean_transactions([5, 20, 100], min_threshold=50), [100])

    def test_empty(self):
        self.assertEqual(clean_transactions([]), [])


class TestFees(unittest.TestCase):
    def test_default_fee(self):
        self.assertEqual(apply_service_fee([100, 250.0]), [98.0, 245.0])

    def test_custom_fee(self):
        self.assertEqual(apply_service_fee([200], fee_rate=0.05), [190.0])

    def test_empty(self):
        self.assertEqual(apply_service_fee([]), [])


class TestNestedTotal(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(calculate_nested_total([]), 0.0)
        self.assertEqual(calculate_nested_total(42), 42)
        self.assertEqual(calculate_nested_total(4.5), 4.5)

    def test_assignment_example(self):
        self.assertEqual(calculate_nested_total([100, [50, 25], [[10, 5], 40]]), 230)

    def test_deep_and_empty_sublists(self):
        self.assertEqual(calculate_nested_total([[], [5, []], [[], [[], 7]]]), 12)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_nested_total([1, "x"])


if __name__ == "__main__":
    unittest.main()
