---
type: dashboard
tags: [dashboard, moc]
---

# 🛡️ Sami Ali — Cybersecurity Dashboard

> **Last opened:** `= date(today)` | **Active cert:** CCNA | **Internship:** DHS HS-POWER (CBP Vuln Assessment)

---

## 🎯 Current Focus
- **Phase:** 
- **Active Cert:** CCNA (in progress)
- **Next Cert:** AWS Solutions Architect Associate
- **Active Platform:** 
- **Current Project:** 

---

## 📅 Today
```dataviewjs
const today = dv.date("today").toFormat("yyyy-MM-dd");
const file = dv.pages('"00-Dashboard/Daily-Notes"').where(p => p.file.name === today).first();
if (file) {
    dv.paragraph(`✅ [[${file.file.path}|Today's note]] is open`);
} else {
    dv.paragraph(`📝 No daily note yet for ${today}. Click your **Calendar** sidebar → today → create.`);
}
```

---

## 🏆 Cert Progress
| Cert | Status | Target |
|------|--------|--------|
| CompTIA Security+ | ✅ Done | — |
| AWS Cloud Practitioner | ✅ Done | — |
| CCNA | 🔄 In Progress |  |
| AWS SA Associate | ⏳ Not Started |  |
| Splunk Core | ⏳ Not Started |  |
| BTL1 | ⏳ Not Started |  |
| eJPT | ⏳ Not Started |  |
| SC-200 | ⏳ Not Started |  |
| AWS Security Specialty | ⏳ Not Started |  |
| PNPT | ⏳ Not Started |  |
| OSCP | ⏳ Not Started |  |

---

## 📚 Recent CTF Write-Ups
```dataview
TABLE WITHOUT ID
  file.link AS "Machine",
  platform AS "Platform",
  difficulty AS "Difficulty",
  status AS "Status",
  date-completed AS "Completed"
FROM "07-CTF-Writeups"
WHERE type = "ctf-writeup"
SORT date-completed DESC
LIMIT 10
```

---

## 🎣 Recent Phishing Analyses
```dataview
TABLE WITHOUT ID
  file.link AS "Sample",
  source AS "Source",
  verdict AS "Verdict",
  date-analyzed AS "Date"
FROM "03-Phase-6-12-Specialization/Phishing-Analysis"
WHERE type = "phishing-analysis"
SORT date-analyzed DESC
LIMIT 10
```

---

## 📊 Vulnerability Reports
```dataview
TABLE WITHOUT ID
  file.link AS "Report",
  scanner AS "Scanner",
  critical-count AS "Critical",
  high-count AS "High",
  status AS "Status"
FROM ""
WHERE type = "vulnerability-report"
SORT date-scanned DESC
LIMIT 5
```

---

## ✅ Open Tasks Across the Vault
```tasks
not done
limit 15
sort by due
```

---

## 📁 Quick Links
- 📝 [[Templates/CTF-Writeup-Template|CTF Write-Up Template]]
- 🎣 [[Templates/Phishing-Analysis-Template|Phishing Template]]
- 📊 [[Templates/Vulnerability-Report-Template|Vuln Report Template]]
- 📅 [[Templates/Weekly-Review-Template|Weekly Review Template]]
- 🌅 [[Templates/Daily-Note-Template|Daily Note Template]]

### Cheat Sheets
- 🔎 [[11-Resources/Cheat-Sheets/Splunk-SPL-Cheatsheet|Splunk SPL]]
- 🔎 [[11-Resources/Cheat-Sheets/KQL-Cheatsheet|KQL (Sentinel)]]
- 🎯 [[11-Resources/Cheat-Sheets/MITRE-ATT&CK-Reference|MITRE ATT&CK]]

---

## 📈 Vault Stats
```dataviewjs
const total = dv.pages().length;
const ctfs = dv.pages().where(p => p.type === "ctf-writeup").length;
const phish = dv.pages().where(p => p.type === "phishing-analysis").length;
const daily = dv.pages('"00-Dashboard/Daily-Notes"').length;
dv.paragraph(`**${total}** total notes  |  **${ctfs}** CTF write-ups  |  **${phish}** phishing analyses  |  **${daily}** daily notes`);
```

---

## 🗓️ Weekly Focus
**Week of:**  
**Goal this week:**  
**Platform hours:**  
**Cert study hours:**  
**Project worked on:**  
