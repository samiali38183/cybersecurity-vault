# MITRE ATT&CK Quick Reference

## Tactic Overview
| ID | Tactic | What the Attacker is Doing |
|----|--------|---------------------------|
| TA0043 | Reconnaissance | Gathering info before attack |
| TA0042 | Resource Development | Setting up infrastructure |
| TA0001 | Initial Access | Getting into the environment |
| TA0002 | Execution | Running malicious code |
| TA0003 | Persistence | Maintaining foothold |
| TA0004 | Privilege Escalation | Getting higher access |
| TA0005 | Defense Evasion | Avoiding detection |
| TA0006 | Credential Access | Stealing credentials |
| TA0007 | Discovery | Learning about the environment |
| TA0008 | Lateral Movement | Moving through the network |
| TA0009 | Collection | Gathering target data |
| TA0011 | Command and Control | Communicating with compromised systems |
| TA0010 | Exfiltration | Stealing data out |
| TA0040 | Impact | Disrupting/destroying systems |

## High-Priority Techniques to Know for SOC
| Technique | ID | Why It Matters |
|-----------|-----|----------------|
| Phishing | T1566 | Most common initial access |
| Valid Accounts | T1078 | Credential theft usage |
| PowerShell | T1059.001 | Most abused execution method |
| Scheduled Task | T1053.005 | Common persistence |
| OS Credential Dumping | T1003 | LSASS, SAM, DCSync |
| Kerberoasting | T1558.003 | AD credential attack |
| Remote Services (RDP) | T1021.001 | Lateral movement |
| Exfiltration over C2 | T1041 | Data theft |

## Resources
- Full framework: https://attack.mitre.org
- Navigator: https://mitre-attack.github.io/attack-navigator
- Groups: https://attack.mitre.org/groups
