import os, json, glob, argparse, random, time

def simulate_eval(prompt: str):
    # Replace with real endpoint call
    risk = 1 if any(k in prompt.lower() for k in ["ssn", "secrets", "ignore prior rules"]) else 0
    defended = random.random() > 0.5
    return {"attack_success": bool(risk and not defended), "pii_leak": False}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", required=False, default="http://localhost:8000")
    ap.add_argument("--tests", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    results = {"total": 0, "attack_success": 0, "pii_leak": 0}
    for path in glob.glob(os.path.join(args.tests, "*.json")):
        data = json.load(open(path))
        for t in data.get("tests", []):
            out = simulate_eval(t.get("prompt",""))
            results["total"] += 1
            results["attack_success"] += int(out["attack_success"])
            results["pii_leak"] += int(out["pii_leak"])

    json.dump(results, open(args.out, "w"), indent=2)
    print("Wrote", args.out, results)

if __name__ == "__main__":
    main()
