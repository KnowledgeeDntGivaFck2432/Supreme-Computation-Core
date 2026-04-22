from rules import RULES

def evaluate(system):
    invariants = [
        "time", "continuity", "alignment", "genesis",
        "boundary", "reference", "causality", "consciousness"
    ]

    missing = []
    invalid = []

    for i in invariants:
        if i not in system:
            missing.append(i)
        elif system[i] is not True:
            invalid.append(i)

    if missing or invalid:
        return {
            "status": "FRAGMENTED",
            "missing": missing,
            "invalid": invalid,
            "reason": "Invariant violation detected"
        }

    # Rule enforcement
    for rule in RULES:
        if not rule["check"](system):
            return {
                "status": "FRAGMENTED",
                "missing": [],
                "invalid": [],
                "reason": rule["error"]
            }

    return {
        "status": "COHERENT",
        "missing": [],
        "invalid": [],
        "reason": "All invariants satisfied"
    }
