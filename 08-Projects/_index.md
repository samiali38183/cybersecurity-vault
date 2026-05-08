---
type: moc
tags: [moc, projects, portfolio]
---

# 🛠️ Projects

> Portfolio projects. Each project lives in its own folder with full documentation. **Public on GitHub** — recruiters look here.

## Roadmap Projects
- [[Phishing-Analysis-Series]] — Document 10+ real phishing samples with full analysis
- [[Network-Traffic-Analysis]] — Wireshark / Zeek captures from CTFs and home lab
- [[Python-IOC-Extractor]] — Parse phishing emails to pull out and enrich IOCs
- [[Linux-Security-Audit]] — Hardening checklist script for Ubuntu/CentOS
- [[Splunk-Detection-Rules]] — Custom SPL detections you've authored
- [[Sigma-Rules-Library]] — Vendor-agnostic detection rules in Sigma format
- [[AWS-Security-Audit]] — Script to audit IAM, S3, Security Group misconfigs
- [[Vuln-Management-Report]] — End-to-end vuln management deliverable from internship-style scope
- [[Home-Lab-Documentation]] — Document your lab build (network diagram, services, learnings)

## What "done" looks like for each project
1. Working code/output committed to its subfolder
2. A `README.md` in its subfolder with: what it does, how to run it, screenshots
3. (Optional but ideal) A LinkedIn post about it
4. Linked from the [[00-Dashboard/Dashboard|Dashboard]]

## Project Status
```dataview
TABLE WITHOUT ID
  file.link AS "Project",
  status AS "Status",
  github-link AS "GitHub"
FROM "08-Projects"
WHERE type = "project"
```
