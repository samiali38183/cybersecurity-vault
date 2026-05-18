"""IOC Extractor - regex-based extraction of indicators of compromise."""
import re


# ============================================================
# Regex patterns - tuned to avoid common false positives
# ============================================================

IPV4_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

DOMAIN_PATTERN = (
    r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,}\b"
)

URL_PATTERN = r"https?://[^\s<>\"']+"

EMAIL_PATTERN = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

MD5_PATTERN = r"\b[a-fA-F0-9]{32}\b"
SHA1_PATTERN = r"\b[a-fA-F0-9]{40}\b"
SHA256_PATTERN = r"\b[a-fA-F0-9]{64}\b"


def extract_ips(text: str) -> list[str]:
    """Return unique IPv4 addresses found in text, sorted."""
    matches = re.findall(IPV4_PATTERN, text)
    return sorted(set(matches))


def extract_domains(text: str) -> list[str]:
    """Return unique domains found in text, sorted, lowercased."""
    matches = re.findall(DOMAIN_PATTERN, text)
    return sorted({m.lower() for m in matches})


def extract_urls(text: str) -> list[str]:
    """Return unique URLs found in text, sorted."""
    matches = re.findall(URL_PATTERN, text)
    return sorted(set(matches))


def extract_emails(text: str) -> list[str]:
    """Return unique email addresses found in text, sorted, lowercased."""
    matches = re.findall(EMAIL_PATTERN, text)
    return sorted({m.lower() for m in matches})


def extract_hashes(text: str) -> dict:
    """Return dict of hash type -> sorted unique list of hashes."""
    return {
        "md5": sorted(set(re.findall(MD5_PATTERN, text))),
        "sha1": sorted(set(re.findall(SHA1_PATTERN, text))),
        "sha256": sorted(set(re.findall(SHA256_PATTERN, text))),
    }


def extract_all(text: str) -> dict:
    """Run all extractors and return combined results as a dict."""
    return {
        "ips": extract_ips(text),
        "domains": extract_domains(text),
        "urls": extract_urls(text),
        "emails": extract_emails(text),
        "hashes": extract_hashes(text),
    }