# KQL (Kusto Query Language) Cheat Sheet — Microsoft Sentinel

## Basic Syntax
```
TableName
| where TimeGenerated > ago(1h)
| where FieldName == "value"
| project Field1, Field2, Field3
| summarize count() by Field1
| sort by count_ desc
```

## Key Tables in Sentinel
| Table | Contains |
|-------|----------|
| SecurityEvent | Windows Event Logs |
| SigninLogs | Azure AD sign-ins |
| AuditLogs | Azure AD audit events |
| AzureActivity | Azure resource operations |
| CommonSecurityLog | CEF/syslog (firewalls, IDS) |
| DeviceProcessEvents | MDE process creation |
| EmailEvents | Defender for Office 365 |

## Essential Security Queries

### Failed Sign-Ins
```
SigninLogs
| where ResultType != 0
| summarize FailureCount=count() by UserPrincipalName, IPAddress
| where FailureCount > 5
| sort by FailureCount desc
```

### Failed Windows Logins
```
SecurityEvent
| where EventID == 4625
| summarize count() by Account, IpAddress
| where count_ > 10
```

### New User Created
```
SecurityEvent
| where EventID == 4720
| project TimeGenerated, Account, SubjectAccount, Computer
```


