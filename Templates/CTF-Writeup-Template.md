---
type: ctf-writeup
platform:
machine:
difficulty:
category:
status: in-progress
date-started: <% tp.date.now("YYYY-MM-DD") %>
date-completed:
tags: [ctf, writeup]
mitre-techniques: []
---

# CTF Write-Up: <% tp.file.title %>

> **Platform:** | **Difficulty:** | **Category:** | **Date Completed:**

---

## Summary
One paragraph: what the machine/challenge was, what the key vulnerability or technique was, what you learned.

---

## Enumeration
### Port Scan
```
nmap -sC -sV -oN nmap_initial.txt <IP>
```

### Service Enumeration
Document what you found on each open port.

---

## Exploitation
### Vulnerability Identified
What was the vuln? CVE if applicable. MITRE ATT&CK technique if applicable.

### Steps to Exploit
Step by step. Include commands. Include relevant output.

---

## Privilege Escalation
What path did you take? What tool identified it (LinPEAS / WinPEAS / manual)?

---

## Flags
- [ ] User flag
- [ ] Root flag

---

## Key Takeaways
- What did you learn that you didn't know before?
- What would you do differently?
- What technique will you use again?

---

## MITRE ATT&CK Mapping
| Technique | ID | Tactic |
|-----------|-----|--------|
|           |    |        |

---

## Tools Used
- 

---

## Related Notes
- 
