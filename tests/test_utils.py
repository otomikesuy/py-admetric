from unittest import TestCase
from py_admetric import utils


# Not expecting negative value
class TestUtils(TestCase):
    def test_safe_div(self):
        test_cases = [
            {
                "name": "standard_case: numerator is zero value",
                "args": {
                    "numerator": 0,
                    "denominator": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: denominator is zero value",
                "args": {
                    "numerator": 100,
                    "denominator": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both of numerator and denominator are zero value",
                "args": {
                    "numerator": 0,
                    "denominator": 0,
                },
                "want": 0.0,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # standard cases
                actual = utils.safe_div(target_test["args"]["numerator"], target_test["args"]["denominator"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_validate_negative(self):
        test_cases = [
            {
                "name": "standard_case: a is zero value",
                "args": {
                    "a": 0,
                    "b": 100,
                },
                "want_error": False,
            },
            {
                "name": "standard_case: b is zero value",
                "args": {
                    "a": 100,
                    "b": 0,
                },
                "want_error": False,
            },
            {
                "name": "standard_case: both of a and b are zero value",
                "args": {
                    "a": 0,
                    "b": 0,
                },
                "want_error": False,
            },
            {
                "name": "standard_case: a is less than zero",
                "args": {
                    "a": -1,
                    "b": 0,
                },
                "want_error": True,
                "error_type": ValueError,
            },
            {
                "name": "standard_case: b is less than zero",
                "args": {
                    "a": 0,
                    "b": -1,
                },
                "want_error": True,
                "error_type": ValueError,
            },
            {
                "name": "standard_case: both of a and b iare less than zero",
                "args": {
                    "a": -1,
                    "b": -1,
                },
                "want_error": True,
                "error_type": ValueError,
            },
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # cases which raises error
                if target_test.get("want_error", False):
                    with self.assertRaises(target_test["error_type"]):
                        utils.validate_negative(target_test["args"]["a"], target_test["args"]["b"])
                    continue

                # cases which returns None
                actual = utils.validate_negative(target_test["args"]["a"], target_test["args"]["b"])
                self.assertIsNone(actual)

    def test_validate_integer(self):
        test_cases = [
            {
                "name": "standard_case: both of a and b are integer value",
                "args": {
                    "a": 200,
                    "b": 100,
                },
                "want_error": False,
            },
            {
                "name": "standard_case: a is string value",
                "args": {
                    "a": "aa",
                    "b": 0,
                },
                "want_error": True,
                "error_type": ValueError
            },
            {
                "name": "standard_case: both of a and b are string value",
                "args": {
                    "a": "aa",
                    "b": "aw",
                },
                "want_error": True,
                "error_type": ValueError
            },
            {
                "name": "standard_case: both of a and b are float value",
                "args": {
                    "a": 1.11,
                    "b": 1.12,
                },
                "want_error": True,
                "error_type": ValueError
            },
            {
                "name": "standard_case: a is a list of integer",
                "args": {
                    "a": [1],
                    "b": 1,
                },
                "want_error": True,
                "error_type": ValueError
            },
            {
                "name": "standard_case: b is a dict",
                "args": {
                    "a": {"a": 1, "b": 2},
                    "b": 1,
                },
                "want_error": True,
                "error_type": ValueError
            },
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # cases which raises error
                if target_test.get("want_error", False):
                    with self.assertRaises(target_test["error_type"]):
                        utils.validate_integer(target_test["args"]["a"], target_test["args"]["b"])
                    continue

                # cases which returns None
                actual = utils.validate_integer(target_test["args"]["a"], target_test["args"]["b"])
                self.assertIsNone(actual)
