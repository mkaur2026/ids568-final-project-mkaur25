# IDS 568 Final Project

## Overview
This project implements a production-ready LLM inference system with monitoring, A/B testing, governance, drift detection, and risk assessment.

The system is built on top of a FastAPI-based LLM inference server (from Milestone 5) and extends it with full MLOps capabilities required for real-world deployment.

---

## System Architecture
User → FastAPI Server → Batching Layer → LLM Model → Output  
Monitoring via Prometheus metrics

---

## Components

### Component 1: Production Monitoring
- Implemented Prometheus-based monitoring
- Tracks:
  - Request count (`llm_requests_total`)
  - Latency distribution (`llm_request_latency_seconds`)
- Exposes `/metrics/` endpoint
- Includes traffic simulation for testing

### Component 2: A/B Testing
- Simulated experiment comparing:
  - Baseline batching vs improved batching
- Used:
  - Two-proportion Z-test
  - t-test for latency
- Result:
  - ~4% improvement in success rate
  - Reduced latency
- Decision: **Ship treatment**

### Component 3: Model Card & Governance
- Model card documenting:
  - Model details
  - Intended use
  - Limitations and risks
- Risk register covering:
  - Performance, reliability, and ethical risks
- Audit trail for system changes

### Component 4: Drift Detection
- Implemented PSI (Population Stability Index)
- Result:
  - PSI = 0.8597 → significant drift
- Includes visualization of distribution shift
- Provides recommendations for retraining and monitoring

### Component 5: Risk Assessment
- System-level risk analysis
- Covers:
  - Hallucination risk
  - Performance risks
  - Data drift risks
- Includes:
  - Risk matrix
  - Governance review
  - CTO recommendation memo

---

## Setup Instructions

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn src.server:app --reload
```

---

## Key Features
- Real-time monitoring with Prometheus metrics
- Traffic simulation for load testing
- Statistical A/B testing framework
- Drift detection using PSI
- Full governance and documentation
- Risk analysis and mitigation strategies

---

## Reproducibility

Run the following scripts:

```bash
python src/monitoring/generate_traffic.py
python src/ab_test/simulation.py
python src/drift/drift_detection.py
```

---


