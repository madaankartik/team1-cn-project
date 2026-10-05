# DNS Verification - Mac 1

The following was verified on 5 October 2026:

```text
Command: dig @10.7.9.180 app.team1.test
Status: NOERROR
Flags: qr aa rd ra
Answer: app.team1.test. 0 IN A 10.7.19.111
Server: 10.7.9.180#53
Query time: 1 msec
```

This confirms that Mac 1's `dnsmasq` service answers the private project record authoritatively on port `53`.
