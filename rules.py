 RULES = [
    {
        "name": "causality_requires_time_and_continuity",
        "check": lambda s: not (s.get("causality") and (not s.get("time") or not s.get("continuity"))),
        "error": "Causality cannot exist without time and continuity"
    }
]
