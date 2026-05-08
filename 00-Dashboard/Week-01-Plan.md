---
type: weekly-plan
week: 1
month: 1
focus: Foundation Solidification — Linux + Python kickoff
status: active
---

# 🗓️ Week 1 — Foundation Kickoff

> **Theme:** Get Linux fluency to a real level + start writing Python beyond Java I. Make sure the floor is solid.
>
> **Hours target:** 30 hours of focused work + DHS internship + school as separate commitments.
>
> **Ship by Sunday night:** Bandit levels 0–15 complete + 2 Python scripts in `08-Projects/`.

---

## Daily Schedule

### **Monday — Linux Day 1**
**Goal:** Get into the right headspace + start OverTheWire Bandit

**Tasks:**
- [ ] Read about OverTheWire: https://overthewire.org/wargames/bandit/
- [ ] SSH into Bandit and complete **levels 0 through 5** (first 6 levels)
- [ ] In your vault, create `01-Phase-0-3-Foundation/Linux/Bandit-Walkthrough.md` and document EACH level — the command you used, why it worked, and what you learned
- [ ] Open `00-Dashboard/Skills-Validation-Matrix.md` — check off Linux fundamentals as 🟡 in progress

**Time estimate:** 4 hours

---

### **Tuesday — Linux Day 2**
**Goal:** Push Bandit, learn one new tool deeply

**Tasks:**
- [ ] Bandit **levels 6–11**
- [ ] Document each in your Bandit walkthrough file
- [ ] **Deep-dive ONE tool:** `find` — read `man find`, write 5 example commands in `01-Phase-0-3-Foundation/Linux/find-cheatsheet.md`
- [ ] Daily note in `00-Dashboard/Daily-Notes/` — what clicked, what didn't

**Time estimate:** 5 hours

---

### **Wednesday — Linux Day 3 + Python Kickoff**
**Goal:** Finish first half of Bandit, start Python

**Tasks:**
- [ ] Bandit **levels 12–15**
- [ ] Install Python 3.12 if you haven't, set up `~/Documents/cybersecurity-vault/08-Projects/Python-Practice/`
- [ ] Write **Script #1: `log_grep.py`** — takes a log file path and a regex pattern, prints matching lines with line numbers. Use argparse. ~40 lines.
- [ ] Add a README.md to `08-Projects/Python-Practice/` explaining what's there

**Time estimate:** 6 hours

---

### **Thursday — Python Real Practice**
**Goal:** Write Script #2 — something you'd actually use

**Tasks:**
- [ ] **Script #2: `port_scanner.py`** — given an IP and port range, uses `socket` to check which ports are open. ~60 lines. Add timeouts so it doesn't hang.
- [ ] Test it against `scanme.nmap.org` (legal to scan — it's their lab target).
- [ ] Write a real README.md for the script: what it does, how to run, sample output (paste a screenshot of it running).

**Time estimate:** 5 hours

---

### **Friday — Wireshark Intro + Networking Brain**
**Goal:** Get hands on a packet capture

**Tasks:**
- [ ] Install Wireshark
- [ ] Capture 30 seconds of your own browsing traffic
- [ ] Filter to just HTTP — what do you see?
- [ ] Filter to just DNS — what queries?
- [ ] Document what you found in `01-Phase-0-3-Foundation/Networking/wireshark-first-capture.md` (sanitize anything personal!)
- [ ] Read CCNA chapter for the day (continue your normal CCNA flow)

**Time estimate:** 4 hours

---

### **Saturday — LOCK IN DAY 🔒**
**Goal:** 6+ hours of pure project work. No videos, no passive consumption.

**Tasks:**
- [ ] Bandit **levels 16–20** (push as far as you can)
- [ ] **Script #3: `ip_extractor.py`** — reads any text file (logs, emails, anything), extracts all valid IP addresses, prints unique ones with counts. This is the foundation of your future IOC Extractor project.
- [ ] **Pick 1 TryHackMe room** from the *Pre-Security* path or *Introduction to Cyber Security* path. Complete it.
- [ ] Write a brief writeup in `06-Labs-and-Platforms/TryHackMe/`

**Time estimate:** 6+ hours

---

### **Sunday — Reflect + Plan Week 2**
**Goal:** Lock in what you learned, plan ahead

**Tasks:**
- [ ] Open `00-Dashboard/Skills-Validation-Matrix.md` — update statuses
- [ ] Write a **Weekly Review** using the [[Templates/Weekly-Review-Template|Weekly Review Template]]. Save it in `00-Dashboard/Daily-Notes/Weekly-Reviews/`
- [ ] Push everything to GitHub: `Ctrl+P → Git: Create backup`
- [ ] Verify on GitHub: https://github.com/samiali38183/cybersecurity-vault — should see a week's worth of commits
- [ ] Plan Week 2 (I'll give you the plan but you should know what's coming)

**Time estimate:** 2 hours

---

## End of Week 1 — What You Should Have Shipped

✅ **In your vault on GitHub:**
- `01-Phase-0-3-Foundation/Linux/Bandit-Walkthrough.md` (levels 0–20+)
- `01-Phase-0-3-Foundation/Linux/find-cheatsheet.md`
- `01-Phase-0-3-Foundation/Networking/wireshark-first-capture.md`
- `08-Projects/Python-Practice/log_grep.py` + README
- `08-Projects/Python-Practice/port_scanner.py` + README + screenshot
- `08-Projects/Python-Practice/ip_extractor.py` + README
- `06-Labs-and-Platforms/TryHackMe/[room-name].md`
- 7 daily notes in `00-Dashboard/Daily-Notes/`
- 1 weekly review

✅ **Skills matrix updates:**
- Linux fundamentals: ❌ → 🟡
- Python: 🟡 → 🟢 (you'll have 3 working scripts!)
- Wireshark: ❌ → 🟡

---

## Rules for Week 1

1. **No copy-paste from ChatGPT/Claude into your project code.** You can use AI to explain concepts, debug your own code, or review what you wrote — but you write it. Recruiters can sniff out AI-generated portfolio code in 30 seconds.

2. **Commit AT LEAST once per day.** `Ctrl+P → Git: Create backup` from Obsidian. End of day, repo shows you worked that day.

3. **Every Python script gets a README.** "Here's what it does. Here's how to run it. Here's sample output." This is the minimum bar.

4. **If you get stuck on Bandit > 30 minutes, ask me.** Don't waste hours. But TRY for 30 min first.

5. **Daily note every day.** Even 3 sentences.

---

## Week 2 Preview
- Finish Bandit (all levels)
- Linux Journey full course
- 2 more Python scripts (file integrity checker + a hash cracker against your own test data)
- 1st HackTheBox easy box (Linux-based — likely "Lame" or "Bashed")
