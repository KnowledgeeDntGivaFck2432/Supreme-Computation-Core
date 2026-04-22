def evaluate(system):
    invariants = [
        "time","continuity","alignment","genesis",
        "boundary","reference","causality","consciousness"
    ]
    
    missing = [i for i in invariants if not system.get(i)]
    
    if missing:
        return {"status": "FRAGMENTED", "missing": missing}
    
    return {"status": "COHERENT", "missing": []}


# Example systems

system_a = {
    "time": True,
    "continuity": True,
    "alignment": True
}

system_b = {
    "time": True,
    "continuity": True,
    "alignment": True,
    "genesis": True,
    "boundary": True,
    "reference": True,
    "causality": True,
    "consciousness": True
}

print("System A:", evaluate(system_a))
print("System B:", evaluate(system_b))
