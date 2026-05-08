---
type: skills-matrix
tags: [skills, validation, interview-prep]
---

# 🎯 Skills Validation Matrix

> Every skill claimed on the README and resume needs a **proof artifact** in this vault. If a skill exists on the resume but not in this matrix, it's a lie. Don't lie on resumes.
>
> **Status meanings:**
> - ❌ Not started
> - 🟡 Learning, no proof yet
> - 🟢 Proven — artifact exists in vault, can defend in interview

---

## Vulnerability Management

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| Nessus operation | DHS internship work + lab scan documented in `06-Labs-and-Platforms` | 🟡 |
| CVSS scoring | Vuln-Report-Template filled out for 3+ samples | ❌ |
| EPSS prioritization | Written explanation + example in `03-Phase-6-12-Specialization/Vulnerability-Management` | ❌ |
| CISA KEV | Cross-reference in any vuln writeup | ❌ |
| Vuln prioritization workflow | Documented end-to-end in a vuln report | ❌ |

## SIEM / Detection

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| Splunk SPL — basic | 30+ documented searches in cheat sheet | ❌ |
| Splunk SPL — security | Full BOTS v1 writeup | ❌ |
| Microsoft Sentinel KQL | 30+ documented queries + working Sentinel lab | ❌ |
| Sigma rule authoring | 20+ original Sigma rules in `08-Projects/Sigma-Rules-Library/` | ❌ |
| MITRE ATT&CK mapping | Every CTF writeup mapped + ATT&CK reference doc | 🟡 (doc started) |

## Cloud Security — AWS

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| IAM | Hands-on lab + policy review writeup | ❌ |
| CloudTrail | Detection rule written for CloudTrail events | ❌ |
| GuardDuty | Configured in personal AWS, sample finding documented | ❌ |
| Security Hub | Configured in personal AWS, integration writeup | ❌ |
| S3 controls | Hardening writeup | ❌ |
| AWS Security Audit script | Working tool in `08-Projects/AWS-Security-Audit/` | ❌ |

## Cloud Security — Azure

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| Microsoft Sentinel | Lab build + connector setup writeup | ❌ |
| Microsoft Defender | Defender for Cloud lab walkthrough | ❌ |
| Entra ID | Conditional Access policy walkthrough | ❌ |

## Languages

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| Python | 3+ working tools in `08-Projects/` with tests | 🟡 (Java I coursework only — needs upgrade) |
| Bash | Linux Security Audit script written in Bash or hybrid | ❌ |
| PowerShell | At least one PowerShell script for AD/Windows audit | ❌ |
| SQL | Read 100 queries, write 20 — basic CRUD is enough | ❌ |

## Networking

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| TCP/IP | CCNA cert | 🟡 (in progress) |
| Routing & switching | CCNA cert | 🟡 |
| Subnetting | CCNA cert + manual practice log | 🟡 |
| Wireshark | Practical Packet Analysis book complete + 3 captures analyzed | ❌ |

## Operating Systems

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| Linux fundamentals | OverTheWire Bandit complete + Linux Journey | ❌ |
| Linux security hardening | CIS audit script in `08-Projects/Linux-Security-Audit/` | ❌ |
| Windows | Sec+ + 1 Windows-focused HTB box writeup | 🟡 |
| Active Directory | Home AD lab + 4 AD HTB boxes (Sauna, Forest, Active, Mantis) | ❌ |

## Frameworks

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| NIST 800-53 | Sec+ + control mapping in vuln reports | 🟡 |
| NIST 800-61 (IR) | IR runbook written for 1 attack scenario | ❌ |
| CIS Controls | CIS audit script implementation | ❌ |
| OWASP Top 10 | PortSwigger Academy Top 10 path complete | ❌ |

## Offensive Foundation (so defense decisions are informed)

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| HTB easy boxes (Linux) | 5+ writeups | ❌ |
| HTB easy boxes (Windows) | 3+ writeups | ❌ |
| HTB AD chain | 4 AD box writeups with detection rules | ❌ |
| eJPT cert (optional) | Pass | ❌ |

## SOC / IR

| Skill | Proof Artifact | Status |
|-------|---------------|--------|
| LetsDefend SOC analyst alerts | 10+ resolved with writeups | ❌ |
| Phishing analysis | 10 samples through full triage | ❌ |
| BTL1 cert | Pass | ❌ |

---

## How to use this matrix

- **Once a week:** open this file, check what's still ❌ or 🟡, and decide what next week pushes to 🟢
- **Before any interview:** read this top to bottom. Every 🟢 is something you can confidently discuss
- **Update after every project ships:** flip ❌ → 🟡 (started) or 🟡 → 🟢 (proven)
- **No 🟢 without an artifact in this vault.** Period.

---

## Interview readiness threshold

**Security Analyst / SOC role:** ~70% of items at 🟢
**Detection Engineer:** Detection-focused rows at 🟢, plus 50% of others
**Security Engineer (entry):** ~80% at 🟢, including at least one 🟢 in each major section
**Cloud Security Engineer:** AWS section fully 🟢, Azure section 50%+
