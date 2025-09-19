package llm.policies

deny[msg] {
  input.findings[_].severity == "high"
  msg := "High-severity finding blocks release"
}
