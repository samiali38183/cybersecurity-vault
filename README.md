<div align="center">

# Sami Ali

### Cybersecurity Professional · DHS Vulnerability Assessment Intern

[![Security+](https://img.shields.io/badge/CompTIA%20Security%2B-Certified-E2231A?style=for-the-badge&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/security)
[![AWS CCP](https://img.shields.io/badge/AWS%20Cloud%20Practitioner-Certified-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/certification/certified-cloud-practitioner/)
[![Network+](https://img.shields.io/badge/CompTIA%20Network%2B-In%20Progress-009BA8?style=for-the-badge&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/network)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sami-ali-1a4b89345)

</div>

---

## Profile

Cybersecurity student working on the **U.S. Department of Homeland Security / CBP Vulnerability Assessment Team** through the **HS-POWER program**. Currently focused on **defensive security engineering** — detection content, security automation, and cloud security — with a target of a Security Engineer / Detection Engineer internship for Summer 2027.

NOVA Cybersecurity student (3.65 GPA, Dean's List ×4), transferring to George Mason University through the Mason Advance Program.

This repository is my **portfolio output** — shipped projects, completed labs, and reference content. Study notes and personal materials live elsewhere.

---

## 🛠️ Featured Project

### [Phishing IOC Extractor](./08-Projects/Phishing-IOC-Extractor)

Python CLI that parses raw `.eml` phishing samples and extracts indicators of compromise — IPv4 addresses, domains, URLs, emails, and MD5/SHA-1/SHA-256 hashes — into deduplicated JSON for downstream threat intel workflows.

**Stack:** Python stdlib only (`re`, `email`, `argparse`, `json`, `pathlib`) · 10 pytest tests passing · MIT licensed

```console
$ python main.py sample_phishing.txt --pretty
{
  "ips": ["192.168.1.100", "203.0.113.45"],
  "domains": ["evil-domain.org", "malicious-cdn.evil", "paypa1-fake.com"],
  "urls": ["http://paypa1-fake.com/login", "https://malicious-cdn.evil/payload.exe"],
  "emails": ["help@evil-domain.org", "paypal-security@paypa1-fake.com", "victim@example.com"],
  "hashes": {
    "md5": ["5d41402abc4b2a76b9719d911017c592"],
    "sha1": ["aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"],
    "sha256": ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]
  }
}
```

→ [View full project + source](./08-Projects/Phishing-IOC-Extractor)

---

## 🏅 Certifications

### Earned
- **CompTIA Security+** (CE)
- **AWS Certified Cloud Practitioner**

### In Progress (2026)
- **CompTIA Network+** — target pass May 2026
- **Splunk Core Certified User** — target pass June 2026
- **Microsoft SC-200** (Security Operations Analyst) — Microsoft Learn path

### Planned (2026-2027)
- **BTL1** — Blue Team Level 1 (hands-on defensive cert)
- **AWS Solutions Architect Associate**
- **AWS Security Specialty**
- **Microsoft SC-300** — Identity and Access Administrator
- **Microsoft AZ-500** — Azure Security
- **Splunk Enterprise Security Certified Admin**

---

## 🚩 Active Practice & CTFs

Currently building methodology and writeup library across:

- **TryHackMe** — Pre-Security path → SOC Level 1 path
- **picoCTF** — General Skills, Cryptography, Web Exploitation
- **HackerOne CTF (Hacker101)** — planned for bug-bounty fundamentals
- **HackTheBox** — TJNull's beginner Linux list (planned post-Net+)
- **LetsDefend** — SOC analyst alert investigations (planned)

Completed writeups will ship to [`07-CTF-Writeups/`](./07-CTF-Writeups) as they are finished.

---

## 💼 Experience

### Vulnerability Assessment Intern — Department of Homeland Security
**U.S. Customs and Border Protection · HS-POWER Program** · Ashburn, VA · *Summer 2026*

Working on the CBP Vulnerability Assessment Team supporting federal-scale vulnerability management operations. Hands-on exposure to enterprise scanning, CVSS-based triage, and remediation workflows within a federal cybersecurity environment.

### IT Support — Heavenly Touch Homecare
*Fairfax, VA · May 2024 – Present*

Endpoint and network support for a healthcare operations team: workstation provisioning, user access management, hardware troubleshooting, network connectivity.

---

## 🎓 Education

**Northern Virginia Community College** · *Expected May 2026*
Information Technology · Cybersecurity Minor
**GPA: 3.65** · **Dean's List × 4** · **Mason Advance Program** (guaranteed GMU transfer)

**Relevant Coursework:** Linux System Administration · Network Security Basics · PC Hardware & OS Architecture · Microcomputer Operating Systems · Java Programming I

---

## 🎯 Areas of Focus

- **Detection Engineering** — Sigma rule authoring, MITRE ATT&CK mapping, SIEM detection logic
- **Cloud Security** — AWS native security tooling (IAM, CloudTrail, GuardDuty, Security Hub, S3 controls)
- **Vulnerability Management** — applied work via DHS / CBP
- **Security Automation** — Python tooling for log parsing, IOC enrichment, audit checks
- **Active Directory & Windows Internals** — authentication flows, attack chains, event log analysis

---

## 🧰 Technical Stack

**Languages:** Python · Bash · PowerShell · SQL fundamentals
**Security:** Vulnerability management workflows · CVSS · EPSS · CISA KEV · MITRE ATT&CK · regex-driven IOC extraction
**SIEM (building):** Splunk SPL · Microsoft Sentinel KQL · Sigma rules
**Cloud:** AWS (IAM, EC2, S3, VPC, CloudTrail, CCP-level) · Azure familiarity
**Networking:** TCP/IP · OSI · subnetting · routing & switching · VLANs · ACLs · Wireshark
**Operating Systems:** Linux (Ubuntu, Kali) · Windows (incl. Active Directory)
**Frameworks:** NIST 800-53 · NIST 800-61 · CIS Controls · OWASP Top 10
**Tools:** Git · GitHub · VS Code · VirtualBox · pytest

---

## 📂 Repository Map

| Path | Contents |
|------|----------|
| [`08-Projects/`](./08-Projects) | Original security tooling (Python) — shipped & tested |
| [`07-CTF-Writeups/`](./07-CTF-Writeups) | Completed CTF and lab walkthroughs (in progress) |
| [`11-Resources/`](./11-Resources) | Curated cheat sheets — Splunk SPL · KQL · MITRE ATT&CK |
| [`Templates/`](./Templates) | Documentation templates for consistent write-ups |

---

## 📬 Contact

- **LinkedIn:** [linkedin.com/in/sami-ali-1a4b89345](https://www.linkedin.com/in/sami-ali-1a4b89345)
- **GitHub:** [@samiali38183](https://github.com/samiali38183)
- **Email:** Available on request via LinkedIn

---

<div align="center">

*All work in this repository is original. Lab and CTF content is conducted in legal lab environments.*

</div>
