import json
import sys
from demo import evaluate

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_sc.py '<json_system>'")
        print("Example:")
        print('python run_sc.py \'{"time": true, "continuity": true}\'')
        return

    try:
        system = json.loads(sys.argv[1])
    except Exception as e:
        print("Invalid JSON input:", e)
        return

    result = evaluate(system)

    print("\nSC Evaluation Result:")
    print(json.dumps(result, indent=2))

    if result["status"] == "FRAGMENTED":
        print("\nFragmentation detected due to missing invariants.")
    else:
        print("\nSystem is coherent.")

if __name__ == "__main__":
    main()
