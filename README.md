# README.md: DNS over TLS proxy

- Listens for DNS queries on port 53/tcp 
- Uses Cloudflare 1.1.1.1 over TCP/TLS 1.3 to resolve requests.

## security

- does not use DNSSEC. Resolved Addresses may be altered by privileged attacker.
- does not use blacklists/whitelists

## future-work

- Add UDP handelling
- Add Caching
- Add Proper logging
- Add Error handelling
- Add Sane tests

## run // build // deploy

```
docker-compose up
```

## test

```
watch dig +tcp @localhost example.com
```
