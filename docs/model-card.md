# Model Card: LLM Inference System (Milestone 5)

## Model Details
- Model Name: sshleifer/tiny-gpt2
- Model Type: Transformer-based causal language model
- Framework: Hugging Face Transformers
- Deployment: FastAPI server with batching and caching

## Intended Use
Primary Use:
- Text generation for demonstration and testing purposes

Out-of-Scope:
- Production-grade decision making
- Sensitive or high-stakes applications
- Legal, medical, or financial advice

## Performance Metrics
- Average latency: ~100–120 ms (local CPU)
- Success rate: ~87%–91% based on simulated A/B testing
- Supports batching and caching optimizations

## Training Data
The model is a pre-trained open-source model from Hugging Face.  
Training data is not controlled or curated in this project.

## Limitations
- Very small model → low quality text generation
- Not suitable for real-world applications
- May produce repetitive or nonsensical output
- No grounding or factual verification

## Ethical Considerations
- Potential for generating misleading or incorrect information
- No safeguards against harmful or biased content
- Not designed for fairness or bias mitigation

## Failure Modes
- Repetitive output (e.g., repeated tokens)
- Poor coherence for longer prompts
- Sensitivity to prompt wording

## System Context
The model is deployed within a FastAPI-based inference system with:
- Dynamic batching
- Request caching
- Monitoring via Prometheus metrics
