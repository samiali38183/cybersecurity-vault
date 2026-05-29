# Screenshots — capture checklist

Drop your real screenshots here as you build and run the lab. The main README references each by filename. Capture these:

- [ ] `01-vms-running.png` — VirtualBox dashboard, all 4 VMs running
- [ ] `02-dc-promoted.png` — Server Manager showing AD DS role + corp.lab domain
- [ ] `03-client-joined.png` — Win10 System properties showing domain membership
- [ ] `04-splunk-ingest.png` — Splunk search showing events from both hosts
- [ ] `05-bruteforce-detection.png` — Splunk dashboard with Event ID 4625 spike
- [ ] `06-kerberoast-detection.png` — Splunk showing 4769 RC4 ticket requests
- [ ] `07-asrep-detection.png` — Splunk showing 4768 no-preauth requests
- [ ] `08-lateral-detection.png` — Splunk showing PsExec service creation (7045)
- [ ] `09-persistence-detection.png` — Splunk showing 4698 scheduled task creation

**Tip:** Use `Win + Shift + S` to snip, paste into Paint, save as PNG with the exact filename above. Once all are in, remove the `<!-- SCREENSHOT -->` comment lines in the main README and replace each with `![description](screenshots/filename.png)`.
