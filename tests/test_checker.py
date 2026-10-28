
import unittest
from phishing_checker import inspect_url


class TestPhishingChecker(unittest.TestCase):

    def test_normal_https_sample(self):
        result = inspect_url("https://www.example.com/login")
        self.assertTrue(
            any("No listed warning signs" in item for item in result)
        )

    def test_ip_address_and_http(self):
        result = inspect_url("http://192.0.2.10/account")
        self.assertTrue(any("IP address" in item for item in result))
        self.assertTrue(any("Uses HTTP" in item for item in result))

    def test_at_symbol_and_http(self):
        result = inspect_url(
            "http://example.com@sample.invalid/login"
        )
        self.assertTrue(any("@ symbol" in item for item in result))
        self.assertTrue(any("Uses HTTP" in item for item in result))

    def test_many_hostname_segments(self):
        result = inspect_url(
            "https://a.b.c.d.e.example.invalid/path"
        )
        self.assertTrue(
            any("hostname segments" in item for item in result)
        )

    def test_punycode_marker(self):
        result = inspect_url("https://xn--example.invalid/")
        self.assertTrue(
            any("punycode" in item for item in result)
        )

    def test_long_url(self):
        url = "https://example.com/" + ("a" * 100)
        result = inspect_url(url)
        self.assertTrue(
            any("over 100 characters" in item for item in result)
        )

    def test_empty_input(self):
        result = inspect_url("")
        self.assertEqual(result, ["No URL entered."])


if __name__ == "__main__":
    unittest.main()
