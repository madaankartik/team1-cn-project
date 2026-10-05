# Mac 1 - Private DNS and Test Client

**Owner:** Chirag Lalwani

1. Install `dnsmasq` on Mac 1.
2. Copy `dns/dnsmasq.conf` to the active dnsmasq configuration directory.
3. Copy `dns/team1.hosts` to `/opt/homebrew/etc/dnsmasq.d/team1.hosts` on Apple Silicon, or adjust the path for Intel Homebrew.
4. Start/restart dnsmasq and set at least two client Macs to use `10.7.9.180` as DNS.
5. Verify:

```bash
dig @10.7.9.180 app.team1.test
dig @10.7.9.180 api.team1.test
```

Both names must return `10.7.19.111`.
