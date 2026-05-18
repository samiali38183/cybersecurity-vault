"""Tests for IOC extractor functions."""
import sys
from pathlib import Path

# Make src importable
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from extractor import (
    extract_ips,
    extract_domains,
    extract_urls,
    extract_emails,
    extract_hashes,
    extract_all,
)


def test_extract_ips_basic():
    text = "Server 192.168.1.100 and 10.0.0.5 contacted host."
    assert extract_ips(text) == ["10.0.0.5", "192.168.1.100"]


def test_extract_ips_deduplicates():
    text = "1.1.1.1 and 1.1.1.1 again, then 2.2.2.2"
    assert extract_ips(text) == ["1.1.1.1", "2.2.2.2"]


def test_extract_ips_empty():
    assert extract_ips("no IPs here") == []


def test_extract_urls():
    text = "Visit http://evil.com/path and https://bad.org/login"
    result = extract_urls(text)
    assert "http://evil.com/path" in result
    assert "https://bad.org/login" in result


def test_extract_emails():
    text = "Contact help@example.com or admin@bad-domain.org"
    result = extract_emails(text)
    assert "help@example.com" in result
    assert "admin@bad-domain.org" in result


def test_extract_emails_lowercased():
    text = "Email: ADMIN@EXAMPLE.COM"
    assert extract_emails(text) == ["admin@example.com"]


def test_extract_hashes_md5():
    text = "MD5 is 5d41402abc4b2a76b9719d911017c592 in this sample."
    result = extract_hashes(text)
    assert "5d41402abc4b2a76b9719d911017c592" in result["md5"]


def test_extract_hashes_all_types():
    text = (
        "MD5: 5d41402abc4b2a76b9719d911017c592 "
        "SHA1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d "
        "SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
    result = extract_hashes(text)
    assert len(result["md5"]) == 1
    assert len(result["sha1"]) == 1
    assert len(result["sha256"]) == 1


def test_extract_all_returns_all_keys():
    result = extract_all("Test")
    assert "ips" in result
    assert "domains" in result
    assert "urls" in result
    assert "emails" in result
    assert "hashes" in result


def test_empty_text_returns_empty_results():
    result = extract_all("")
    assert result["ips"] == []
    assert result["urls"] == []
    assert result["emails"] == []
    assert result["hashes"]["md5"] == []
    assert result["hashes"]["sha1"] == []
    assert result["hashes"]["sha256"] == []
