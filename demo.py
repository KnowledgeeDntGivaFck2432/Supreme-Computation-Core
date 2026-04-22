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
            "invalid": invalid
        }

    return {
        "status": "COHERENT",
        "missing": [],
        "invalid": []
    }
