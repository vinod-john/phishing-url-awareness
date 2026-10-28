
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Inspect URL text for common phishing warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in parsed.netloc:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: Long URL
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IPv4 hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Many hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 48)
    print("PHISHING URL AWARENESS CHECKER")
    print("=" * 48)
    print("Local URL-text analysis only.")
    print("This program does not open URLs or contact websites.")

    while True:
        raw_url = input(
            "\nEnter a sample URL (or q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")

        for finding in findings:
            print("- " + finding)

        # Improvement: summary message
        informational = (
            "No URL entered.",
            "Could not identify",
            "This text is not a valid URL",
            "No listed warning signs found."
        )

        has_warnings = any(
            not finding.startswith(informational)
            for finding in findings
        )

        if has_warnings:
            print("\nREVIEW CAREFULLY")
            print("One or more warning indicators were found.")

        print("\nRemember: warning indicators are not proof.")
        print("Never enter passwords on unexpected websites.")


if __name__ == "__main__":
    main()
