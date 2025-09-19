# Securing LLM Applications with a DevSecOps Framework

This starter repo scaffolds a reference RAG + tool-use LLM application with a **DevSecOps** pipeline:
- SBOM + signing (Syft/Grype/Trivy + Cosign)
- Policy-as-code (OPA/Rego) + Kubernetes admission
- Guardrails (input/output validators, PII scrubber, tool sandbox)
- Adversarial eval harness (prompt-injection, jailbreaks, privacy leakage)
- IaC (Terraform/Helm) and runtime hardening (NetworkPolicies, non-root, seccomp)

> Generated on 2025-09-19. Fill in credentials and replace placeholders before running in production.

## Structure
```
infra/
  terraform/
  helm/
  .github/workflows/
app/
  _init_.py
  api/
  _init_.py
  llm/
security/
  policies/
  schemas/
evals/
  adversarial/
  harness/
docs/
scripts/
```

## Quick start
1. Install Docker, kubectl, helm, cosign, syft, grype, trivy, conftest.
2. Create a registry (e.g., GHCR) and set `MODEL_ENDPOINT` & secrets in CI.
3. `helm upgrade --install llmapp infra/helm` after CI passes.
