# Splunk SPL Cheat Sheet

## Basic Search Syntax
```
index=<index> sourcetype=<sourcetype> field=value
```

## Essential Commands
| Command | What It Does | Example |
|---------|-------------|---------|
| stats | Aggregate data | `stats count by src_ip` |
| eval | Create/modify fields | `eval risk=if(count>10,"high","low")` |
| rex | Extract fields with regex | `rex field=_raw "(?P<ip>\d+\.\d+\.\d+\.\d+)"` |
| table | Display specific fields | `table _time, src_ip, user, action` |
| sort | Sort results | `sort -count` |
| dedup | Remove duplicates | `dedup src_ip` |
| transaction | Group related events | `transaction src_ip maxspan=5m` |
| lookup | Enrich with external data | `lookup threat_intel ip AS src_ip` |
| timechart | Time-based chart | `timechart count by action` |
| where | Filter results | `where count > 5` |

## Key Security Searches

### Failed Logins (Windows)
```
index=windows EventCode=4625
| stats count by src_ip, user
| where count > 5
| sort -count
```

### Brute Force + Success Pattern
```
index=windows (EventCode=4625 OR EventCode=4624)
| stats count(eval(EventCode=4625)) AS failures,
        count(eval(EventCode=4624)) AS successes by user, src_ip
| where failures > 5 AND successes > 0
```

### New Local Admin Created
```
index=windows EventCode=4720 OR EventCode=4732
| table _time, user, src_user, host
```

### Scheduled Task Created
```
index=windows EventCode=4698
| table _time, host, user, Task_Name, Task_Content
```

### PowerShell Execution
```
index=windows EventCode=4688 New_Process_Name="*powershell*"
| table _time, host, user, Command_Line
```

## Add your own searches below as you learn them
