<div align="center">

# Sami Ali

### Cybersecurity Engineer · DHS Vulnerability Assessment Intern

[![Security+](https://img.shields.io/badge/CompTIA%20Security%2B-Certified-E2231A?style=for-the-badge&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/security)
[![AWS CCP](https://img.shields.io/badge/AWS%20Cloud%20Practitioner-Certified-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/certification/certified-cloud-practitioner/)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sami-ali-1a4b89345)

</div>

---

## Profile

Cybersecurity engineer working on the **U.S. Department of Homeland Security / CBP Vulnerability Assessment Team** through the **HS-POWER program**. Focus areas: detection engineering, security automation, and cloud security.

3.65 GPA at Northern Virginia Community College · Dean's List × 4 · Mason Advance Program (guaranteed transfer to George Mason University).

---

## 🛠️ Featured Project

### [Phishing IOC Extractor](./08-Projects/Phishing-IOC-Extractor)

A Python CLI that parses raw `.eml` phishing samples and extracts indicators of compromise — IPv4 addresses, domains, URLs, email addresses, and MD5/SHA-1/SHA-256 hashes — into deduplicated JSON for downstream threat intel workflows.

- Python stdlib only (`re`, `email`, `argparse`, `json`, `pathlib`) — zero external runtime dependencies
- RFC 822 `.eml` parsing with multipart body handling
- 10 pytest tests covering each extractor and edge cases — all passing
- Type-hinted, docstring'd, MIT licensed

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

→ [View source, tests, and full documentation](./08-Projects/Phishing-IOC-Extractor)

---

## 🏅 Certifications

- **CompTIA Security+** (CE)
- **AWS Certified Cloud Practitioner**

---

## 💼 Experience

### Vulnerability Assessment Intern · Department of Homeland Security
**U.S. Customs and Border Protection · HS-POWER Program** · Ashburn, VA · Summer 2026

Operating on the CBP Vulnerability Assessment Team supporting federal-scale vulnerability management operations. Hands-on with enterprise scanning, CVSS-based triage, and remediation tracking workflows in a federal cybersecurity environment.

### IT Support · Heavenly Touch Homecare
Fairfax, VA · May 2024 – Present

Endpoint and network support for a healthcare operations team — workstation provisioning, user access management, hardware and connectivity troubleshooting.

---

## 🎓 Education

**Northern Virginia Community College** — Information Technology (Cybersecurity minor)
GPA: **3.65** · Dean's List × 4 · Mason Advance Program

**Relevant coursework:** Linux System Administration · Network Security Basics · PC Hardware & OS Architecture · Microcomputer Operating Systems · Java Programming I

---

## 🧰 Technical Stack

**Vulnerability Management:** enterprise scanning workflows · CVSS triage · CISA KEV · NIST 800-53 control awareness
**Languages:** Python · Bash · PowerShell
**Cloud:** AWS (IAM, EC2, S3, VPC, CloudTrail fundamentals) — CCP certified
**Networking:** TCP/IP · OSI · subnetting · routing & switching · VLANs · ACLs
**Operating Systems:** Linux (Ubuntu) · Windows
**Security Tooling:** regex-driven IOC extraction · MITRE ATT&CK technique mapping · `.eml` / RFC 822 email parsing
**Frameworks:** NIST 800-53 · OWASP Top 10 · CIA Triad · defense in depth
**Engineering:** Git · GitHub · pytest · type hints · CLI design with argparse · MIT-licensed open source

---

## 📂 Repository Map

| Path | Contents |
|------|----------|
| [`08-Projects/`](./08-Projects) | Shipped security tooling — Python, tested, documented |
| [`07-CTF-Writeups/`](./07-CTF-Writeups) | Completed CTF and lab walkthroughs |
| [`11-Resources/`](./11-Resources) | Curated reference — Splunk SPL · KQL · MITRE ATT&CK |
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
