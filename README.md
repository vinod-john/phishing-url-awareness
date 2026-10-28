# EWB Phishing URL Awareness Checker

## Overview

Phishing is a common cyberattack in which attackers use fake or misleading links to trick users into sharing sensitive information, such as passwords and banking details.

The **EWB Phishing URL Awareness Checker** is a Python-based command-line project that checks URL text for common phishing warning signs. I developed this project to understand basic phishing indicators and improve cybersecurity awareness. The program analyzes the URL locally without opening websites or sending network requests.

## Features

The project includes the following features:

- Detects the `@` symbol in the URL authority.
- Identifies unusually long URLs containing more than 100 characters.
- Detects IPv4 addresses used as hostnames.
- Flags hostnames containing five or more segments.
- Identifies punycode-style hostnames containing `xn--`.
- Warns when a URL uses the HTTP scheme.
- Allows users to check multiple URLs in one session.
- Displays a **REVIEW CAREFULLY** message when warning indicators are detected.
- Provides a reminder that warning indicators do not prove a URL is malicious.

## Technologies Used

- **Programming language:** Python
- **Interface:** Command-line interface (CLI)
- **Libraries:** Python standard libraries
- **Testing:** Python `unittest` framework

## Requirements

- Python 3.10 or later.
- No additional packages or API keys are required.

## Project Structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   ├── test_checker.py
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## How to Run the Project

### Step 1: Open the project folder

Open the `phishing-url-awareness` folder in Visual Studio Code or a terminal.

### Step 2: Run the Python program

**Windows**

```bash
python phishing_checker.py
```

**macOS/Linux**

```bash
python3 phishing_checker.py
```

### Step 3: Enter a sample URL

Enter a URL when the program prompts you. The program displays any detected warning indicators.

To exit the program, enter `q`.

## Example Execution

The following example demonstrates the expected output when checking a sample URL:

```text
================================================
PHISHING URL AWARENESS CHECKER
================================================
Local URL-text analysis only.
This program does not open URLs or contact websites.

Enter a sample URL (or q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY
One or more warning indicators were found.

Remember: warning indicators are not proof.
Never enter passwords on unexpected websites.
```

## Testing

I prepared manual test cases and automated tests to check the program's behavior.

To run the automated tests, execute the following command from the project root directory:

```bash
python -m unittest discover -s tests -v
```

The test cases cover:

1. A sample HTTPS URL with no listed warning indicators.
2. A URL containing an IP-address hostname and using HTTP.
3. A URL containing an `@` symbol and using HTTP.
4. A hostname with five or more segments.
5. A hostname containing the `xn--` punycode marker.
6. A URL longer than 100 characters.
7. Empty input.

The manual test cases and expected results are documented in `tests/test_samples.md`.

Actual test results should be recorded after running the program and test suite.

## Screenshots

The `screenshots` folder contains evidence of program execution and testing.

### Sample Program Run

![Sample program run](screenshots/sample_run.png)

### Automated Test Results

![Automated test results](screenshots/test_results.png)

These images should be captured from the actual program and test execution.

## Improvements Implemented

### 1. Repeated URL Checking

I added a loop that allows users to check multiple URLs without restarting the application. Users can enter `q` to exit the program.

**Verification:** Enter multiple sample URLs in one session and confirm that the program continues until the exit command is entered.

### 2. Warning Summary

I added a `REVIEW CAREFULLY` message when one or more warning indicators are detected. This makes the output easier to understand for beginners.

**Verification:** Enter the sample URL `http://192.0.2.10/account` and check that the IP-address warning, HTTP warning, and summary message are displayed.

## Limitations

This project is intended for educational and cybersecurity awareness purposes.

- It analyzes URL text only.
- It does not visit websites or send network requests.
- It does not scan for malware or verify website ownership.
- It cannot guarantee whether a URL is safe or malicious.
- Legitimate URLs may trigger warnings, and malicious URLs may not trigger any of the implemented checks.

**Important:** No listed warning signs found does not mean that a URL is safe.

## Ethical Use

This project is intended for defensive cybersecurity learning. Use sample URL strings for demonstrations and testing. Do not collect credentials, deceive users, or test websites without permission.

## Author

Name:Darvemula Vinod
Course/Batch:
Program:EWB Courses — Cybersecurity Mini Project