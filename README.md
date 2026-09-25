# Synthetic multi-repository security lab: gateway

Deliberately vulnerable, synthetic code for authorized static-analysis testing. Do not expose or deploy this lab. No real customer data or secrets are present.

The gateway authenticates through identity, forwards authenticated requests to the service named in `/api/<service>/<path>`, and returns the downstream status, body, content type and location. Identity supplies X-User-Id to downstream services.

## Repository map

- [gateway](https://github.com/sainath1204/cr-multirepo-lab-gateway)
- [identity](https://github.com/sainath1204/cr-multirepo-lab-identity)
- [orders](https://github.com/sainath1204/cr-multirepo-lab-orders)
- [files](https://github.com/sainath1204/cr-multirepo-lab-files)
- [fetch](https://github.com/sainath1204/cr-multirepo-lab-fetch)
- [templates](https://github.com/sainath1204/cr-multirepo-lab-templates)
- [jobs](https://github.com/sainath1204/cr-multirepo-lab-jobs)
- [archives](https://github.com/sainath1204/cr-multirepo-lab-archives)
- [redirects](https://github.com/sainath1204/cr-multirepo-lab-redirects)
- [search](https://github.com/sainath1204/cr-multirepo-lab-search)
