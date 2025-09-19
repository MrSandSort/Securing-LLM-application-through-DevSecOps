# Guardrails and policy helpers (stubs)
ALLOWED_TOOLS = {"search": True, "weather": True}

def allow_tool(name: str) -> bool:
  return name in ALLOWED_TOOLS
