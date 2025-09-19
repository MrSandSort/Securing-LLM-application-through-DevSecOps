# Threat Model (STRIDE + LLM-specific)
- Spoofing: API key theft, prompt spoofing
- Tampering: poisoned RAG docs, modified prompts
- Repudiation: insufficient audit logs
- Information disclosure: PII leakage, prompt leaks
- DoS: prompt bombs, token floods
- Elevation: tool abuse

Mitigations mapped to pipeline and runtime controls.
