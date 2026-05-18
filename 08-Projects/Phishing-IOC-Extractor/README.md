# Phishing IOC Extractor

A Python CLI tool that parses phishing emails (or any text input) and extracts indicators of compromise (IOCs): IPv4 addresses, domains, URLs, email addresses, and file hashes (MD5, SHA-1, SHA-256). Produces clean, deduplicated JSON ready for downstream threat intel enrichment.

## Why I built this

Phishing triage begins with extracting IOCs from raw email content. Doing this by hand is slow and error-prone — every analyst writes some version of this script eventually. This tool automates the regex-heavy first step so an analyst can move directly to enrichment and decision-making.

Built as a portfolio piece while studying for a defensive cybersecurity role.

## Features

- Parses raw `.eml` files (RFC 822 email format) — extracts headers + plaintext body
- Falls back to plain-text mode for any non-`.eml` input
- Extracts:
  - IPv4 addresses
  - Domains
  - URLs (http / https)
  - Email addresses
  - File hashes — MD5, SHA-1, SHA-256
- Deduplicates and sorts every output category
- JSON output (compact or pretty-printed)
- Optional `-o` flag to write directly to a file
- Stdlib-only — zero external runtime dependencies

## Quick start

```bash
# From repo root
cd 08-Projects/Phishing-IOC-Extractor/src

# Run against the included sample
python main.py ../samples/sample_phishing.txt --pretty

# Or save the report to a file
python main.py ../samples/sample_phishing.txt --pretty -o report.json
```

## Demo

A live run against the included `sample_phishing.txt` fake phishing email:

```console
PS C:\Users\samis\Documents\cybersecurity-vault\08-Projects\Phishing-IOC-Extractor\src> python main.py ..\samples\sample_phishing.txt --pretty
{
  "ips": [
    "192.168.1.100",
    "203.0.113.45"
  ],
  "domains": [
    "evil-domain.org",
    "example.com",
    "malicious-cdn.evil",
    "payload.exe",
    "paypa1-fake.com"
  ],
  "urls": [
    "http://paypa1-fake.com/login",
    "https://malicious-cdn.evil/payload.exe"
  ],
  "emails": [
    "help@evil-domain.org",
    "paypal-security@paypa1-fake.com",
    "victim@example.com"
  ],
  "hashes": {
    "md5": [
      "5d41402abc4b2a76b9719d911017c592"
    ],
    "sha1": [
      "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
    ],
    "sha256": [
      "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    ]
  }
}
```

One command in, structured IOC report out. Ready for downstream enrichment (VirusTotal lookups, threat intel correlation, blocklist generation).

## Sample output (compact reference)

```json
{
  "ips": [
    "192.168.1.100",
    "203.0.113.45"
  ],
  "domains": [
    "evil-domain.org",
    "malicious-cdn.evil",
    "paypa1-fake.com"
  ],
  "urls": [
    "http://paypa1-fake.com/login",
    "https://malicious-cdn.evil/payload.exe"
  ],
  "emails": [
    "help@evil-domain.org",
    "paypal-security@paypa1-fake.com",
    "victim@example.com"
  ],
  "hashes": {
    "md5": ["5d41402abc4b2a76b9719d911017c592"],
    "sha1": ["aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"],
    "sha256": ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]
  }
}
```

## CLI usage

```
usage: main.py [-h] [-o OUTPUT] [--pretty] file

Extract IOCs (IPs, domains, URLs, emails, hashes) from a file.

positional arguments:
  file                 Path to input file (.eml, .txt, or any text)

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  Output file path (default: stdout)
  --pretty             Pretty-print JSON output
```

## Tests

10 pytest tests covering each extractor function and edge cases (deduplication, empty input, lowercased outputs, all three hash types).

```bash
pip install pytest
cd 08-Projects/Phishing-IOC-Extractor
python -m pytest tests/ -v
```

All tests run in under a second.

## How it works

The core engine (`src/extractor.py`) uses tuned regex patterns for each IOC type:

| IOC Type | Pattern Logic |
|----------|---------------|
| IPv4 | Four dot-separated groups of 1-3 digits, with `\b` boundaries to avoid matching inside longer numbers |
| Domain | Letter / digit / hyphen labels separated by dots, ending in a 2+ letter TLD |
| URL | `http://` or `https://` followed by non-whitespace characters |
| Email | Standard RFC-style local-part `@` domain pattern |
| MD5 / SHA-1 / SHA-256 | Hex strings of exact lengths 32, 40, and 64 |

Each extractor deduplicates with `set()` and returns a sorted list (or dict for hashes).

For `.eml` files, the stdlib `email` module parses the message structure. Headers and plain-text body are concatenated before extraction runs.

## Project structure

```
Phishing-IOC-Extractor/
├── README.md
├── LICENSE
├── requirements.txt        (stdlib-only — empty)
├── .gitignore
├── src/
│   ├── extractor.py        ← regex engine + extraction functions
│   └── main.py             ← CLI entry point
├── samples/
│   └── sample_phishing.txt ← dummy phishing test data
└── tests/
    └── test_extractor.py   ← pytest test suite
```

## Tested on

- Python 3.14
- Windows 11
- Ubuntu 22.04

## Known limitations (v1)

- Domain regex can match dotted strings that aren't real domains (e.g., `payload.exe`) — a TLD whitelist is planned for v2
- HTML email body parsing not yet supported (only `text/plain`)
- Defanged IOC support (e.g., `hxxp://evil[.]com`) not yet supported

## Roadmap (v2 ideas)

- TLD whitelist using IANA's public list to eliminate false positives
- VirusTotal / AbuseIPDB / URLhaus enrichment via API calls
- Defanged IOC normalization (`hxxp://evil[.]com` → `http://evil.com`)
- HTML email body parsing with `BeautifulSoup`
- MITRE ATT&CK technique tagging per IOC type
- Simple Streamlit web UI

## License

MIT — see `LICENSE`.
