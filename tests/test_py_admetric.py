from unittest import TestCase
from py_admetric import py_admetric


class TestPyAdmetric(TestCase):
    def test_cpi(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "impressions": 0,
                    "cost": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "impressions": 1000,
                    "cost": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "impressions": 1,
                    "cost": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "impressions": 10,
                    "cost": 19,
                },
                "want": 1.9,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "impressions": 112,
                    "cost": 199,
                },
                "want": 1.7767857142857142,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "impressions": 9388,
                    "cost": 1003,
                },
                "want": 0.10683851725607157,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "impressions": 1938401,
                    "cost": 4850184,
                },
                "want": 2.502157190385271159,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "impressions": 2123940192,
                    "cost": 4810433195,
                },
                "want": 2.264862830469004091,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "impressions": -9388,
                    "cost": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "impressions": 132123,
                    "cost": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "impressions": -19299381,
                    "cost": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "impressions": 1929.9381,
                    "cost": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "impressions": 19299381,
                    "cost": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "impressions": 192.99381,
                    "cost": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.cpi(target_test["args"]["cost"], target_test["args"]["impressions"])
                    continue

                # standard cases
                actual = py_admetric.cpi(target_test["args"]["cost"], target_test["args"]["impressions"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_cpm(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "impressions": 0,
                    "cost": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "impressions": 1000,
                    "cost": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "impressions": 1,
                    "cost": 1,
                },
                "want": 1000.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "impressions": 10,
                    "cost": 19,
                },
                "want": 1900.00,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "impressions": 112,
                    "cost": 199,
                },
                "want": 1776.7857142857142,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "impressions": 9388,
                    "cost": 1003,
                },
                "want": 106.83851725607157,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "impressions": 1938401,
                    "cost": 4850184,
                },
                "want": 2502.157190385271159,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "impressions": 2123940192,
                    "cost": 4810433195,
                },
                "want": 2264.862830469004091,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "impressions": -9388,
                    "cost": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "impressions": 132123,
                    "cost": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "impressions": -19299381,
                    "cost": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "impressions": 1929.9381,
                    "cost": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "impressions": 19299381,
                    "cost": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "impressions": 192.99381,
                    "cost": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.cpi(target_test["args"]["cost"], target_test["args"]["impressions"])
                    continue

                # standard cases
                actual = py_admetric.cpm(target_test["args"]["cost"], target_test["args"]["impressions"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_cpc(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "clicks": 0,
                    "cost": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "clicks": 1000,
                    "cost": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "clicks": 1,
                    "cost": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "clicks": 10,
                    "cost": 19,
                },
                "want": 1.9,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "clicks": 112,
                    "cost": 199,
                },
                "want": 1.7767857142857142,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "clicks": 1112,
                    "cost": 9999,
                },
                "want": 8.991906474820144,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "clicks": 1938401,
                    "cost": 4850184,
                },
                "want": 2.502157190385271159,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "clicks": 3123940192,
                    "cost": 7911043319,
                },
                "want": 2.532392694091629,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "clicks": -9388,
                    "cost": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "clicks": 132123,
                    "cost": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "clicks": -19299381,
                    "cost": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "clicks": 1929.9381,
                    "cost": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "clicks": 19299381,
                    "cost": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "clicks": 192.99381,
                    "cost": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.cpc(target_test["args"]["cost"], target_test["args"]["clicks"])
                    continue

                # standard cases
                actual = py_admetric.cpc(target_test["args"]["cost"], target_test["args"]["clicks"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_cpa(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "conversions": 0,
                    "cost": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "conversions": 1000,
                    "cost": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "conversions": 1,
                    "cost": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "conversions": 10,
                    "cost": 19,
                },
                "want": 1.9,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "conversions": 112,
                    "cost": 199,
                },
                "want": 1.7767857142857142,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "conversions": 1112,
                    "cost": 9999,
                },
                "want": 8.991906474820144,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "conversions": 1938401,
                    "cost": 4850184,
                },
                "want": 2.502157190385271159,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "conversions": 3123940192,
                    "cost": 7911043319,
                },
                "want": 2.532392694091629,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "conversions": -9388,
                    "cost": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "conversions": 132123,
                    "cost": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "conversions": -19299381,
                    "cost": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "conversions": 1929.9381,
                    "cost": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "conversions": 19299381,
                    "cost": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "conversions": 192.99381,
                    "cost": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.cpa(target_test["args"]["cost"], target_test["args"]["conversions"])
                    continue

                # standard cases
                actual = py_admetric.cpa(target_test["args"]["cost"], target_test["args"]["conversions"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_cpv(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "video_views": 0,
                    "cost": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "video_views": 1000,
                    "cost": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "video_views": 1,
                    "cost": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "video_views": 10,
                    "cost": 19,
                },
                "want": 1.9,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "video_views": 112,
                    "cost": 199,
                },
                "want": 1.7767857142857142,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "video_views": 1112,
                    "cost": 9999,
                },
                "want": 8.991906474820144,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "video_views": 1938401,
                    "cost": 4850184,
                },
                "want": 2.502157190385271159,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "video_views": 3123940192,
                    "cost": 7911043319,
                },
                "want": 2.532392694091629,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "video_views": -9388,
                    "cost": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "video_views": 132123,
                    "cost": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "video_views": -19299381,
                    "cost": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "video_views": 1929.9381,
                    "cost": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "video_views": 19299381,
                    "cost": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "video_views": 192.99381,
                    "cost": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]

            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.cpv(target_test["args"]["cost"], target_test["args"]["video_views"])
                    continue

                # standard cases
                actual = py_admetric.cpv(target_test["args"]["cost"], target_test["args"]["video_views"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_ctr(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "clicks": 0,
                    "impressions": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "clicks": 1000,
                    "impressions": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "clicks": 1,
                    "impressions": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "clicks": 10,
                    "impressions": 19,
                },
                "want": 0.5263157894736842,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "clicks": 112,
                    "impressions": 199,
                },
                "want": 0.5628140703517588,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "clicks": 1112,
                    "impressions": 9999,
                },
                "want": 0.1112111211121112,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "clicks": 1938401,
                    "impressions": 4850184,
                },
                "want": 0.3996551471036975,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "clicks": 3123940192,
                    "impressions": 7911043319,
                },
                "want": 0.3948834642956908,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "clicks": -9388,
                    "impressions": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "clicks": 132123,
                    "impressions": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "clicks": -19299381,
                    "impressions": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "clicks": 1929.9381,
                    "impressions": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "clicks": 19299381,
                    "impressions": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "clicks": 192.99381,
                    "impressions": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]
            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.ctr(target_test["args"]["clicks"], target_test["args"]["impressions"])
                    continue

                # standard cases
                actual = py_admetric.ctr(target_test["args"]["clicks"], target_test["args"]["impressions"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_vtr(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "video_views": 0,
                    "impressions": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "video_views": 1000,
                    "impressions": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "video_views": 1,
                    "impressions": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "video_views": 10,
                    "impressions": 19,
                },
                "want": 0.5263157894736842,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "video_views": 112,
                    "impressions": 199,
                },
                "want": 0.5628140703517588,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "video_views": 1112,
                    "impressions": 9999,
                },
                "want": 0.1112111211121112,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "video_views": 1938401,
                    "impressions": 4850184,
                },
                "want": 0.3996551471036975,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "video_views": 3123940192,
                    "impressions": 7911043319,
                },
                "want": 0.3948834642956908,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "video_views": -9388,
                    "impressions": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "video_views": 132123,
                    "impressions": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "video_views": -19299381,
                    "impressions": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "video_views": 1929.9381,
                    "impressions": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "video_views": 19299381,
                    "impressions": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "video_views": 192.99381,
                    "impressions": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]
            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.vtr(target_test["args"]["video_views"], target_test["args"]["impressions"])
                    continue

                # standard cases
                actual = py_admetric.vtr(target_test["args"]["video_views"], target_test["args"]["impressions"])
                self.assertEqual(actual, target_test["want"], target_test["name"])

    def test_cvr(self):
        test_cases = [
            {
                "name": "standard_case: denominator is zero value",
                "description": "impression value is zero",
                "args": {
                    "conversions": 0,
                    "clicks": 100,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: numerator is zero value",
                "description": "cost value is zero",
                "args": {
                    "conversions": 1000,
                    "clicks": 0,
                },
                "want": 0.0,
            },
            {
                "name": "standard_case: both ones place",
                "description": "impression value is ones place, and also cost value is ones place",
                "args": {
                    "conversions": 1,
                    "clicks": 1,
                },
                "want": 1.00,
            },
            {
                "name": "standard_case: both tens place",
                "description": "impression value is tens place, and also cost value is tens place",
                "args": {
                    "conversions": 10,
                    "clicks": 19,
                },
                "want": 0.5263157894736842,
            },
            {
                "name": "standard_case: both hundreds place",
                "description": "impression value is hundreds place, and also cost value is hundreds place",
                "args": {
                    "conversions": 112,
                    "clicks": 199,
                },
                "want": 0.5628140703517588,
            },
            {
                "name": "standard_case: both thousands place",
                "description": "impression value is thousands place, and also cost value is thousands place",
                "args": {
                    "conversions": 1112,
                    "clicks": 9999,
                },
                "want": 0.1112111211121112,
            },
            {
                "name": "standard_case: both millions place",
                "description": "impression value is millions place, and also cost value is millions place",
                "args": {
                    "conversions": 1938401,
                    "clicks": 4850184,
                },
                "want": 0.3996551471036975,
            },
            {
                "name": "standard_case: both billions place",
                "description": "impression value is billions place, and also cost value is billions place",
                "args": {
                    "conversions": 3123940192,
                    "clicks": 7911043319,
                },
                "want": 0.3948834642956908,
            },
            {
                "name": "error_case: denominator is negative value",
                "description": "impression value is negative",
                "args": {
                    "conversions": -9388,
                    "clicks": 1003,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is negative value",
                "description": "cost value is negative",
                "args": {
                    "conversions": 132123,
                    "clicks": -301,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are negative value",
                "description": "cost value is negative",
                "args": {
                    "conversions": -19299381,
                    "clicks": -3848848,
                },
                "want_error": True,
            },
            {
                "name": "error_case: denominator is float value",
                "description": "impressions value is negative",
                "args": {
                    "conversions": 1929.9381,
                    "clicks": 1333231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: numerator is float value",
                "description": "cost value is negative",
                "args": {
                    "conversions": 19299381,
                    "clicks": 13.33231,
                },
                "want_error": True,
            },
            {
                "name": "error_case: both of denominator and numerator are float value",
                "description": "cost value is negative",
                "args": {
                    "conversions": 192.99381,
                    "clicks": 13.33231,
                },
                "want_error": True,
            }
        ]

        test_length = len(test_cases)
        for i in range(test_length):
            target_test = test_cases[i]
            with self.subTest(target_test["name"]):
                # error cases
                if target_test.get("want_error", False):
                    with self.assertRaises(ValueError):
                        py_admetric.cvr(target_test["args"]["conversions"], target_test["args"]["clicks"])
                    continue

                # standard cases
                actual = py_admetric.cvr(target_test["args"]["conversions"], target_test["args"]["clicks"])
                self.assertEqual(actual, target_test["want"], target_test["name"])
