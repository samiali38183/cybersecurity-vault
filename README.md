<div align="center">

# Sami Ali

### Cybersecurity Engineering · DHS HS-POWER Vulnerability Assessment Intern

[![Security+](https://img.shields.io/badge/CompTIA%20Security%2B-Certified-E2231A?style=for-the-badge&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/security)
[![AWS CCP](https://img.shields.io/badge/AWS%20Cloud%20Practitioner-Certified-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/certification/certified-cloud-practitioner/)
[![AWS SAA](https://img.shields.io/badge/AWS%20Solutions%20Architect%20%E2%80%93%20Associate-In%20Progress-lightgrey?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
[![CySA+](https://img.shields.io/badge/CompTIA%20CySA%2B-In%20Progress-lightgrey?style=for-the-badge&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/cybersecurity-analyst)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sami-ali-1a4b89345)

</div>

---

## Profile

DHS HS-POWER intern on the **U.S. Customs and Border Protection Vulnerability Assessment Team** (Summer 2026). Focus: risk-based vulnerability prioritization, detection engineering, and cloud security.

3.65 GPA at Northern Virginia Community College · Dean's List × 4 · Mason Advance Program (guaranteed transfer to George Mason University).

---

## Featured Projects

### [Phishing IOC Extractor](./08-Projects/Phishing-IOC-Extractor)

Python CLI that parses raw `.eml` phishing samples and extracts indicators of compromise — IPv4 addresses, domains, URLs, email addresses, and MD5/SHA-1/SHA-256 hashes — into deduplicated JSON for downstream threat-intel workflows.

- Python standard library only (`re`, `email`, `argparse`, `json`, `pathlib`) — zero runtime dependencies
- RFC 822 `.eml` parsing with multipart body handling
- 10 pytest tests covering each extractor and edge cases — all passing
- Type-hinted, docstring'd, MIT licensed

```console
$ python main.py sample_phishing.txt --pretty
{
  "ips": ["192.168.1.100", "203.0.113.45"],
  "domains": ["evil-domain.org", "malicious-cdn.evil", "paypa1-fake.com"],
  "urls": ["http://paypa1-fake.com/login", "https://malicious-cdn.evil/payload.exe"],
  "emails": ["help@evil-domain.org", "paypal-security@paypa1-fake.com"],
  "hashes": {
    "md5": ["5d41402abc4b2a76b9719d911017c592"],
    "sha1": ["aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"],
    "sha256": ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]
  }
}
```

→ [Source, tests, and full documentation](./08-Projects/Phishing-IOC-Extractor)

---

### [Network Traffic Analysis Lab — Wireshark](./08-Projects/Wireshark-Lab)

Hands-on packet analysis across five protocol scenarios captured live on a personal lab network — TCP three-way handshake, DNS query/response, HTTP request, TLS Client Hello (SNI), and ARP request/reply. Cross-layer analysis showing the full DNS → TCP → TLS flow for a single connection.

- Analyst-relevant indicators: SNI visibility for SOC monitoring of HTTPS traffic, ARP-poisoning signatures (**MITRE ATT&CK T1557.002**)
- Every scenario documented with the display filter, what to look for, and defender relevance
- Real captures with annotated screenshots

→ [Filters, scenarios, and screenshots](./08-Projects/Wireshark-Lab)

---

## Certifications

- **CompTIA Security+** (DoD 8570 approved)
- **AWS Certified Cloud Practitioner**
- **AWS Solutions Architect – Associate** *(in progress)*
- **CompTIA CySA+** *(in progress)*

**Clearance:** CBP Full Background Investigation (BI) — Active · U.S. Citizen

---

## Experience

### Vulnerability Assessment Team Analyst Intern · U.S. Department of Homeland Security
**U.S. Customs and Border Protection · HS-POWER Program** · Ashburn, VA · May 2026 – Aug 2026

- Led an end-to-end Known Exploited Vulnerabilities (KEV) research project matching enterprise-wide Nessus/Tenable scan results against the CISA KEV Catalog, benchmarking remediation performance against **CISA BOD 26-04** to identify outlier systems and aged-finding backlogs.
- Built a multi-page Power BI dashboard integrating CVSS, EPSS, and remediation-age metrics — demonstrating that exploitation likelihood, not severity alone, distinguishes real-world risk — and delivered an executive briefing to technical and leadership audiences.
- Designed a risk-based prioritization methodology weighing KEV status, asset criticality (HVA), internet exposure, EPSS, and CVSS to guide enterprise remediation under federal directives.
- Drafted technical compliance reports on vulnerability findings and remediation recommendations, supporting operations aligned with the **NIST Cybersecurity Framework**, **FedRAMP**, and **Zero Trust architecture**.

---

## Education

**Northern Virginia Community College** — Information Technology (Cybersecurity minor)
GPA: **3.65** · Dean's List × 4 · Mason Advance Program

**Relevant coursework:** Linux System Administration · Network Security Basics · PC Hardware & OS Architecture · Microcomputer Operating Systems · Java Programming I

---

## Technical Stack

**Vulnerability Management:** Nessus · Tenable · CVSS · EPSS · CISA KEV · CISA BOD 26-04 · enterprise remediation workflows
**Compliance & Frameworks:** NIST 800-53 · NIST Cybersecurity Framework · FedRAMP · Zero Trust · MITRE ATT&CK · OWASP Top 10
**Cloud:** AWS (IAM, EC2, S3, VPC, CloudTrail) — Cloud Practitioner certified
**Networking & Packet Analysis:** TCP/IP · OSI · subnetting · routing & switching · Wireshark · DNS · TLS/SNI · ARP
**Programming & Scripting:** Python (`re`, `email`, `argparse`, `pytest`) · Bash · PowerShell · regex · JSON
**Operating Systems:** Linux (Ubuntu, Kali) · Windows + Active Directory fundamentals
**Engineering:** Git · GitHub · pytest · type hints · argparse CLI design · MIT-licensed open source

---

## Contact

- **LinkedIn:** [linkedin.com/in/sami-ali-1a4b89345](https://www.linkedin.com/in/sami-ali-1a4b89345)
- **GitHub:** [@samiali38183](https://github.com/samiali38183)

---

<div align="center">

*All work in this repository is original. Lab captures conducted on personal systems and networks for defensive analysis practice.*

</div>
