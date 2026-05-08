---
type: moc
tags: [moc, resources]
---

# 📚 Resources

> Reference material — cheat sheets, books, tools, useful links. Stuff you look up, not stuff you write.

## Sections
- **Books** — Reading list, summaries, takeaways
- **Cheat-Sheets** — Quick reference (Splunk SPL, KQL, MITRE ATT&CK, etc.)
- **Tools-Reference** — Common tools and how to use them
- **Links-and-Bookmarks** — External URLs you keep returning to

## Cheat Sheets
- 🔎 [[Splunk-SPL-Cheatsheet]]
- 🔎 [[KQL-Cheatsheet]]
- 🎯 [[MITRE-ATT&CK-Reference]]

## All Resources
```dataview
LIST
FROM "11-Resources"
WHERE file.name != "_index"
SORT file.name ASC
```
