# 🦈 Wireshark Network Traffic Analysis Lab

Hands-on packet analysis covering the protocols and patterns a SOC analyst sees daily — how normal traffic looks, how to filter for what matters, and how to spot suspicious activity at the network layer.

> 🔬 **All captures performed on my own lab network and local machine for defensive analysis practice.**

---

## 🎯 What This Lab Covers

| # | Focus | Why it matters for a defender |
|---|-------|-------------------------------|
| 1 | TCP three-way handshake | Foundation of how connections form; spotting incomplete/scan handshakes |
| 2 | DNS query/response | Most C2 and exfil rides DNS; baselining normal lookups |
| 3 | HTTP requests | Cleartext credentials, suspicious user-agents, malicious downloads |
| 4 | TLS handshake | What's still visible when traffic is encrypted (SNI, cert info) |
| 5 | ARP | Local network mapping; detecting ARP spoofing |
| 6 | Port scan signature | What an Nmap scan looks like on the wire |

---

## 🧰 Filters Cheat Sheet (built during this lab)

The Wireshark display filters I used and reference most:

| Goal | Filter |
|------|--------|
| Only HTTP traffic | `http` |
| Only DNS | `dns` |
| TCP SYN packets (connection starts / scans) | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| Traffic to/from one host | `ip.addr == 192.168.56.20` |
| TLS handshakes | `tls.handshake` |
| TLS Client Hello (shows SNI / destination) | `tls.handshake.type == 1` |
| ARP only | `arp` |
| HTTP POST (often logins / form data) | `http.request.method == "POST"` |
| DNS responses with no such name | `dns.flags.rcode == 3` |
| Conversations on a specific port | `tcp.port == 445` |

---

## 🔍 Capture Scenarios

### Scenario 1 — TCP Three-Way Handshake
The foundation of every TCP connection: **SYN → SYN/ACK → ACK.**

- **Filter:** `tcp.flags.syn == 1`
- **What to observe:** Client sends SYN, server replies SYN/ACK, client sends ACK. A flood of SYNs with no completion = scan or SYN flood.

<!-- SCREENSHOT: Wireshark showing the 3 handshake packets → screenshots/01-tcp-handshake.png -->

### Scenario 2 — DNS Query & Response
- **Filter:** `dns`
- **What to observe:** Query (type A) for a hostname, response with the resolved IP. Watch for unusually long subdomains (possible DNS tunneling) or high-frequency lookups to one domain (possible C2 beaconing).

<!-- SCREENSHOT: Wireshark DNS query + response pair → screenshots/02-dns-query.png -->

### Scenario 3 — HTTP Request Analysis
- **Filter:** `http.request`
- **What to observe:** The full request — method, host, URI, User-Agent. HTTP is cleartext, so credentials in a POST are fully visible. Suspicious User-Agents (e.g., `python-requests`, `curl`, custom strings) can flag automated tooling.

<!-- SCREENSHOT: Wireshark HTTP GET request with headers expanded → screenshots/03-http-request.png -->

### Scenario 4 — TLS Handshake (what's visible when encrypted)
- **Filter:** `tls.handshake.type == 1` (Client Hello)
- **What to observe:** Even though the payload is encrypted, the **Server Name Indication (SNI)** reveals the destination domain, and the certificate exchange shows the server's identity. This is how defenders gain visibility into HTTPS without decryption.

<!-- SCREENSHOT: Wireshark TLS Client Hello showing SNI → screenshots/04-tls-handshake.png -->

### Scenario 5 — ARP & Local Network Mapping
- **Filter:** `arp`
- **What to observe:** "Who has 192.168.56.10? Tell 192.168.56.20" requests and replies. Multiple replies for one IP, or rapid ARP announcements, can indicate **ARP spoofing** (a man-in-the-middle technique, MITRE ATT&CK T1557.002).

<!-- SCREENSHOT: Wireshark ARP request/reply → screenshots/05-arp.png -->

### Scenario 6 — Port Scan Signature
Captured an Nmap scan from a second host to see what reconnaissance looks like on the wire.

- **Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0`
- **What to observe:** One source IP sending SYN packets to many destination ports in rapid succession, most receiving RST (closed) responses. This is the classic TCP SYN scan fingerprint — **ATT&CK T1046 (Network Service Discovery).**

<!-- SCREENSHOT: Wireshark showing rapid SYNs across many ports → screenshots/06-port-scan.png -->

---

## 🧠 What I Learned

- The TCP handshake is the baseline — once you know what "normal" looks like, scans and floods are obvious
- DNS is the most abused protocol for covert channels; long/random subdomains and beaconing intervals are the tells
- HTTP exposes everything in cleartext — a single POST capture shows why HTTPS matters
- TLS encryption hides payloads but **not** SNI or certificate metadata — defenders still get destination visibility
- ARP is trust-by-default, which is exactly why ARP spoofing works and why monitoring it matters

---

## 🔗 How This Connects to SOC Work

Packet analysis is the ground truth behind SIEM alerts. When Splunk or Sentinel flags "suspicious outbound connection," the analyst pivots to the packet capture to confirm: Is this real C2? What's the SNI? What's the beacon interval? This lab builds that pivot-and-confirm muscle.

---

## 🛠️ Tools Used

Wireshark · tcpdump · Nmap (for scan generation) · isolated lab network

**Practice data sources for future captures:** malware-traffic-analysis.net (free, labeled real-world PCAPs), Wireshark sample captures.

---

*All captures performed on my own systems and lab network for defensive network-analysis practice.*
