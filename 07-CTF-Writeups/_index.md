---
type: moc
tags: [moc, ctf, writeups]
---

# 🚩 CTF Write-Ups

> Completed challenge writeups. Public on GitHub — this is **portfolio material**.

## Create a new write-up
Navigate into `HackTheBox/`, `TryHackMe/`, or `CyberDefenders/` and create a new note. Templater auto-applies the [[Templates/CTF-Writeup-Template|CTF Write-Up Template]] for you.

## All Write-Ups
```dataview
TABLE WITHOUT ID
  file.link AS "Machine",
  platform AS "Platform",
  difficulty AS "Difficulty",
  category AS "Category",
  status AS "Status",
  date-completed AS "Completed"
FROM "07-CTF-Writeups"
WHERE type = "ctf-writeup"
SORT date-completed DESC
```

## In-Progress
```dataview
LIST file.link
FROM "07-CTF-Writeups"
WHERE type = "ctf-writeup" AND status = "in-progress"
```
