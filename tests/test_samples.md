
# Phishing URL Awareness Checker — Test Samples

These tests use sample URL strings only. The program does not
open URLs or send network requests.

| # | Input | Expected result | Actual result | Status |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; this does not prove safety | Pending execution | Pending |
| 2 | `http://192.0.2.10/account` | IP-address and HTTP warnings | Pending execution | Pending |
| 3 | `http://example.com@sample.invalid/login` | @ symbol and HTTP warnings | Pending execution | Pending |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments warning | Pending execution | Pending |
| 5 | `https://xn--example.invalid/` | Punycode warning | Pending execution | Pending |

## Manual Testing Procedure

1. Run `python phishing_checker.py` from the project root.
2. Enter each sample URL when prompted.
3. Compare the program output with the expected result.
4. Record the actual result in the table.
5. Mark PASS only when the observed output matches the expected result.
6. Type `q` to exit the program.

## Safety Note

These URLs are sample strings for educational testing.
Do not visit them as part of this project.

Warning indicators are not proof that a URL is malicious.
No warning signs found does not prove that a URL is safe.
