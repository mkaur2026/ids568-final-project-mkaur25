# Risk Register

| ID | Risk | Category | Severity | Likelihood | Mitigation |
|----|------|----------|----------|------------|------------|
| R1 | Model generates incorrect or misleading text | Reliability | High | High | Restrict usage to demo purposes only |
| R2 | High latency under heavy load | Performance | Medium | Medium | Use batching and caching mechanisms |
| R3 | Model produces repetitive or low-quality output | Quality | Medium | High | Limit prompt complexity and output length |
| R4 | Lack of monitoring could hide failures | Operations | High | Medium | Use Prometheus monitoring metrics |
| R5 | Potential misuse of generated content | Ethics | Medium | Medium | Clearly define intended use and restrictions |
| R6 | Cache returns stale or incorrect results | Data Integrity | Low | Medium | Use temperature-based cache control |
