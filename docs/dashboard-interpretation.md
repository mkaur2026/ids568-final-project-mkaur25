# Component 1: Production Monitoring Dashboard Interpretation

## System Overview
This project instruments a FastAPI-based LLM inference server using Prometheus metrics. The server exposes a `/generate` endpoint for text generation and a `/metrics/` endpoint for monitoring.

The monitored model is `sshleifer/tiny-gpt2`, which is used as a lightweight local inference model for testing production monitoring concepts.

## Metrics Collected
The monitoring implementation tracks two main metric groups:

1. `llm_requests_total`
   - Counts total LLM requests by status.
   - Status labels include `success` and `error`.

2. `llm_request_latency_seconds`
   - Tracks request latency using a Prometheus histogram.
   - Buckets include 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, and 5.0 seconds.

## Dashboard Health Interpretation
The dashboard shows that the LLM service is responding successfully to simulated traffic. After running the traffic generation script, the `/metrics/` endpoint showed 31 successful requests.

The latency histogram shows that all observed requests completed under 0.1 seconds in this local test environment. This indicates that the lightweight model is operating efficiently for the simulated workload.

## Bottlenecks and Risks
The current system uses a very small test model, so latency is low. In a real production LLM system, larger models would likely introduce higher inference latency, memory pressure, and GPU/CPU bottlenecks.

Potential risks include:
- Increased latency under higher traffic
- Error spikes if the model or batcher fails
- Resource exhaustion if many requests arrive at once
- Cache behavior hiding true model latency for repeated prompts

## Alert Trigger Conditions
In production, I would configure alerts for the following conditions:

- Error rate greater than 5% over a 5-minute window
- P95 latency greater than 2 seconds
- No successful requests for more than 5 minutes
- Sudden request spike above expected traffic baseline
- Repeated failed requests from the `/generate` endpoint

## Design Justification
Prometheus metrics were selected because they are widely used for production monitoring and integrate well with Grafana dashboards. Counters are appropriate for request totals, while histograms are appropriate for latency distributions because they allow percentile-based analysis such as P95 and P99 latency.

This dashboard focuses on observable operational metrics, which can be collected in real time without human evaluation.
