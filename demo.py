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

    if system.get("causality") and (not system.get("time") or not system.get("continuity")):
        return {
            "status": "FRAGMENTED",
            "missing": [],
            "invalid": ["causality"],
            "reason": "Causality cannot exist without time and continuity"
        }

    return {
        "status": "COHERENT",
        "missing": [],
        "invalid": [],
        "reason": "All invariants satisfied"
    }
