# 🛠️ Projects

Original security tooling, detection content, and lab builds.

## Standard format

Each project lives in its own folder with:

- `README.md` — what it does, why it exists, quick-start, sample output
- Working code (Python, Bash, PowerShell, or YAML for detection rules)
- Sample input data + sample output committed
- Tests where applicable
- License header on source files
- Demo screenshot or animated GIF in the README

## Project domains

| Domain | What's covered |
|--------|---------------|
| **Detection Engineering** | Sigma rule libraries, Splunk SPL detections, KQL queries — vendor-agnostic where possible, ATT&CK-mapped |
| **Security Automation** | Python tooling for log parsing, IOC extraction, threat-intel enrichment |
| **Cloud Security** | Audit scripts and detection content for AWS environments — IAM, S3, CloudTrail, Security Groups |
| **System Hardening** | CIS-aligned audit and remediation tooling for Linux endpoints |
| **Lab Documentation** | Architecture, configuration, and learnings from home-lab builds (incl. Active Directory) |

## Engineering bar

Every project here is intended to be **runnable on a fresh clone**. No hardcoded credentials, no half-finished features in main, no missing dependencies. If it ships here, it works.
