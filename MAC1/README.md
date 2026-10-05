# Mac 1 - Private DNS and Test Client

**Owner:** Chirag Lalwani

1. Install `dnsmasq` on Mac 1.
2. Use `/opt/homebrew/etc/dnsmasq.conf` as the active configuration file.
3. Copy `dns/team1.hosts` to `/opt/homebrew/etc/dnsmasq.d/team1.hosts` on Apple Silicon, or adjust the path for Intel Homebrew.
4. Start/restart dnsmasq and set at least two client Macs to use `10.7.9.180` as DNS.
5. Verify:

```bash
dig @10.7.9.180 app.team1.test
dig @10.7.9.180 api.team1.test
```

Both names must return `10.7.19.111`.

## Verified Commands

```bash
sudo dnsmasq --test
sudo brew services restart dnsmasq
sudo lsof -nP -iTCP:53 -iUDP:53
dig @10.7.9.180 app.team1.test
```

The configured upstream resolver is `1.1.1.1`. The verified DNS response is authoritative (`aa`) and returns `10.7.19.111` for `app.team1.test` on port `53`. The committed config uses `local-ttl=0` to match the live Phase 1 DNS response TTL.
