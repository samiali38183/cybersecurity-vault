---
type: roadmap
tags: [roadmap, plan, career]
target-role: Security Engineer (or Security Analyst as stepping stone)
target-date: 2026-06-01
hours-per-week: 50
---

# 🎯 Master Roadmap — Sami Ali → Security Engineer

> **Goal:** Land a Security Engineer / Senior Security Analyst role within 60 days of NOVA graduation (May 2026).
> **Pace:** 50 hrs/week effective (school + DHS internship + ~30 hrs/week self-directed learning).
> **Exit criteria for the program:** Every skill on the README is hands-on defensible in a technical interview, with portfolio artifacts to prove it.

---

## How this works

1. **One month = one major capability gain.** No more, no less.
2. **Every week ships something.** A note, a writeup, a script, a detection rule. If a week doesn't ship, the week didn't count.
3. **Friday night = reflection.** 30 min reviewing what you learned and what didn't click. Logged in `00-Dashboard/Daily-Notes` as a weekly summary.
4. **Saturday = "lock in" day.** 6+ hours of focused project work. No videos, no passive consumption — only doing.
5. **Sunday = light + plan.** Plan the next week. Maybe one HTB box for fun.

---

## 12-Month Plan

### 🟦 Month 1 (now): **Foundation Solidification**
*Make sure the basics are actually solid before stacking advanced stuff on top.*

- ✅ Finish CCNA exam blueprint review (you're already on this)
- 📚 OverTheWire **Bandit** (full set, ~30 levels) — Linux command-line fluency
- 📚 Linux Journey (linuxjourney.com) — full course
- 🐍 Python: write 5 real scripts (file parsers, API callers, log greppers) — no copy-paste from tutorials
- 🚩 First HTB/THM easy box — pick **TryHackMe Pre-Security path** if you've never done one
- 📓 Daily notes every day, weekly review every Sunday

**Month 1 deliverable:** 5 Python scripts in `08-Projects/` + Bandit complete + 1 CTF writeup.

---

### 🟦 Month 2: **CCNA Pass + Networking Deep**
- 🎯 **Pass CCNA** (target exam date end of month)
- 🦈 Wireshark Cert Prep / Practical Packet Analysis book — chapters 1–6
- 📓 Build a network diagram of your home setup with VLANs/subnets

**Month 2 deliverable:** CCNA pass + Wireshark notes file + home network diagram.

---

### 🟦 Month 3: **SOC Fundamentals — Splunk**
- 📚 **Splunk Fundamentals 1** (free, splunk.com/edu)
- 📚 **Splunk Fundamentals 2** (free)
- 🧪 **Splunk BOTS v1** (free dataset on splunk.com) — work through, document every search
- 🎯 Take **Splunk Core Certified User** exam (if free voucher available)
- 📓 Build out `11-Resources/Cheat-Sheets/Splunk-SPL-Cheatsheet.md` with 30+ saved searches

**Month 3 deliverable:** Splunk Core User cert + 30 SPL queries documented + 1 BOTS writeup.

---

### 🟦 Month 4: **SIEM Round 2 — Microsoft Sentinel + KQL**
- 📚 **Microsoft Learn — KQL Quick Reference path** (8 hrs)
- 📚 **SC-200 Microsoft Learn path** (full, ~40 hrs) — this is FREE and excellent
- 🧪 Spin up a free **Sentinel trial** in Azure ($200 free credit) — connect simulated logs
- 📓 Build out KQL cheat sheet to 30+ queries in vault

**Month 4 deliverable:** SC-200 Microsoft Learn complete + working Sentinel lab + 30 KQL queries.

---

### 🟦 Month 5: **Detection Engineering — Sigma + ATT&CK**
- 📚 **MITRE ATT&CK fundamentals** — read the full Enterprise matrix once. No skipping. Take notes.
- 📚 **Sigma rule format** — Florian Roth's Sigma intro talks
- ✍️ **Write 10 original Sigma rules** — covering brute-force, persistence, lateral movement, exfiltration techniques
- 🎯 Take **BTL1 (Blue Team Level 1)** exam
- 📓 Every CTF writeup gets MITRE ATT&CK technique IDs from now on

**Month 5 deliverable:** BTL1 cert + 10 Sigma rules in `08-Projects/Sigma-Rules-Library/` + ATT&CK reference doc updated.

---

### 🟦 Month 6: **Python Security Automation**
*Build the Python projects on the resume. They have to actually exist.*

- 🐍 Build **Python IOC Extractor** — parses raw .eml files, pulls IPs/domains/hashes/URLs, enriches via VirusTotal API, outputs JSON+CSV. Ship to `08-Projects/Python-IOC-Extractor/`.
- 🐍 Build **Linux Security Audit script** — CIS-aligned checks for Ubuntu. Ship to `08-Projects/Linux-Security-Audit/`.
- 🐍 Build a **log parser** — tails auth.log or Sysmon JSON, alerts on suspicious patterns
- 🧪 Write tests for each. Hand-on-heart, both projects work end-to-end.

**Month 6 deliverable:** 3 working Python tools with READMEs, demo screenshots, and tests.

---

### 🟦 Month 7: **Cloud Security — AWS Depth**
- 🎯 **AWS Solutions Architect Associate** — pass it
- 🛡️ Hands-on with: IAM, CloudTrail, Config, GuardDuty, Security Hub, S3 controls, KMS
- 🧪 Build **AWS Security Audit Tool** — Python script using boto3 to flag IAM misconfigs, public S3 buckets, missing logging. Ship to `08-Projects/AWS-Security-Audit/`.

**Month 7 deliverable:** AWS SA Associate cert + working AWS audit tool.

---

### 🟦 Month 8: **Cloud Security — AWS Specialty**
- 🎯 **AWS Security Specialty** — pass it (this is the cert that opens cloud security doors)
- 🧪 Build a **CloudTrail-driven detection** — Sigma-style rule for suspicious API patterns
- 📓 Phishing analysis series — 10 real samples processed through your IOC Extractor

**Month 8 deliverable:** AWS Security Specialty cert + 10 phishing analyses.

---

### 🟦 Month 9: **Offensive Understanding — Active Directory**
- 🧪 Build **home AD lab** — 1 DC, 1 client, vulnerable misconfigurations on purpose
- 🚩 Complete HTB AD path: **Sauna**, **Forest**, **Active**, **Mantis**
- 📓 Write up each box with full ATT&CK mapping AND the detection rule that would have caught the attack
- 🎯 Take **eJPT** if time permits (it's hands-on, not too brutal)

**Month 9 deliverable:** AD lab built + 4 AD writeups with detections + maybe eJPT.

---

### 🟦 Month 10: **Detection Engineering Round 2**
- ✍️ Add 10 more Sigma rules to library — focusing on cloud detections this time
- 🧪 **Atomic Red Team** — execute techniques, write detections for each, prove they fire
- 📓 Build a **personal threat hunting playbook** in `02-Phase-3-6-SOC-Skills/Threat-Intelligence/`

**Month 10 deliverable:** Sigma library at 20+ rules + Atomic Red Team execution log + threat hunt playbook.

---

### 🟦 Month 11: **Polish, Resume, Network, Apply**
- 📝 Update resume with everything shipped — projects with link to GitHub, certs, real numbers
- 💼 LinkedIn refresh — post about projects monthly from now on
- 📞 Reach out to 5 security engineers per week on LinkedIn — informational interviews
- 🎯 Start applying — every Security Analyst, Vulnerability Analyst, SOC Analyst, Detection Engineer, Cloud Security Analyst role you can find
- 🎤 Mock interviews — use Pramp, interviewing.io, or a friend

**Month 11 deliverable:** 50+ applications submitted. 5+ informational interviews done.

---

### 🟦 Month 12: **Interview, Negotiate, Sign**
- 🎤 You should be in interview loops by now. If not, escalate intensity.
- 📚 Brush up: behavioral STAR stories, technical fundamentals you haven't touched in months
- 💰 Negotiate every offer
- 🖊️ Sign

**Month 12 deliverable:** Signed offer.

---

## See also
- [[Skills-Validation-Matrix]] — every claim on the resume mapped to its proof artifact
- [[Week-01-Plan|This week's plan]] — current focus
- [[Dashboard]] — main view
