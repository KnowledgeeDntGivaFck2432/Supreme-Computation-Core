from demo import evaluate

class SupremeComputation:

    def __init__(self):
        self.invariants = [
            "time", "continuity", "alignment", "genesis",
            "boundary", "reference", "causality", "consciousness"
        ]

    def run(self, system):
        result = evaluate(system)

        return {
            "input": system,
            "result": result,
            "coherent": result["status"] == "COHERENT"
        }

    def assert_coherence(self, system):
        result = self.run(system)

        if not result["coherent"]:
            raise Exception(f"Fragmentation detected: {result['result']}")

        return True
