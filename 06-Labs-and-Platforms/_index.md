---
type: moc
tags: [moc, labs]
---

# 🧪 Labs and Platforms

> Notes from hands-on lab platforms. Different from CTF write-ups (which are completed challenges) — this is for in-progress lab notes, methodology, and platform-specific tips.

## Platforms
- [[HackTheBox]] — Active machines, retired boxes, Academy modules
- [[TryHackMe]] — Learning paths, individual rooms
- [[LetsDefend]] — SOC analyst training, real-world alerts
- [[CyberDefenders]] — Blue team labs and forensic challenges
- [[BlueTeamLabs]] — Defensive security challenges
- [[PortSwigger]] — Web security academy
- [[Splunk-BOTS]] — Boss of the SOC challenges
- [[VulnHub]] — Offline VM challenges

## When to put notes here vs `07-CTF-Writeups`
- **Here:** Methodology, platform-specific tools, in-progress notes
- **CTF Write-Ups:** Completed challenge writeups (those go on GitHub for portfolio)

## Recent Lab Notes
```dataview
LIST
FROM "06-Labs-and-Platforms"
WHERE file.name != "_index"
SORT file.mtime DESC
LIMIT 10
```
