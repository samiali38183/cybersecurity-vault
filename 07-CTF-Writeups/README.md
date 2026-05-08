# 🚩 CTF Write-Ups

Original walkthroughs from completed Capture-The-Flag boxes and challenges.

## Standard format

Every write-up follows the same structure:

- **TL;DR** — 3-sentence summary of the box, the path, the key technique
- **Recon** — enumeration commands and what each one revealed
- **Exploitation** — the vulnerability, why it works, exploitation steps including failed attempts
- **Privilege Escalation** — discovery and exploitation of the priv-esc path
- **MITRE ATT&CK Mapping** — every technique mapped to T-numbers
- **Detection** — the Sigma rule, Splunk search, or KQL query that would catch this attack
- **Lessons Learned** — what was new, what to do differently next time

## Folder structure

| Path | Contents |
|------|----------|
| `HackTheBox/` | HTB box walkthroughs — Active Directory, Linux, Windows |
| `TryHackMe/` | TryHackMe room walkthroughs |
| `CyberDefenders/` | Blue-team and DFIR challenge analyses |

## Why detection focus

Each write-up doesn't just show how the box was rooted — it includes the detection logic a defender would write to catch the attack chain. Defender's mindset on offensive content.
