# System Boundary Diagram

User → FastAPI Server → Batching Layer → LLM Model → Output

## Description

1. User sends request to `/generate`
2. FastAPI server receives request
3. Request goes through batching system
4. Model generates output
5. Response returned to user

## Monitoring Layer
- Prometheus collects metrics from FastAPI
- Metrics include latency and request counts

## Data Flow Risks
- Input: malformed or unexpected prompts
- Processing: batching delays or failures
- Output: low-quality or incorrect text
