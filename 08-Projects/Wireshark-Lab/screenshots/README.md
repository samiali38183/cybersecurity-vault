# Screenshots — capture checklist

Drop your real Wireshark screenshots here as you complete each capture. The main README references each by filename. Capture these:

- [ ] `01-tcp-handshake.png` — the 3 handshake packets (SYN, SYN/ACK, ACK)
- [ ] `02-dns-query.png` — a DNS query + response pair
- [ ] `03-http-request.png` — an HTTP GET request with headers expanded
- [ ] `04-tls-handshake.png` — a TLS Client Hello showing the SNI
- [ ] `05-arp.png` — an ARP request/reply pair
- [ ] `06-port-scan.png` — rapid SYN packets across many ports (run an Nmap scan against your own lab host)

**Tip:** In Wireshark, apply the display filter, then `File → Export Packet Dissections → As Plain Text` for text, or just snip the packet list + detail pane with `Win + Shift + S`. Save as PNG with the exact filename above. Then replace each `<!-- SCREENSHOT -->` comment in the main README with `![description](screenshots/filename.png)`.
