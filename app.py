from flask import Flask, request, jsonify
from sc_engine import SupremeComputation

app = Flask(__name__)
sc = SupremeComputation()

@app.route("/evaluate", methods=["POST"])
def evaluate_system():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "ERROR",
            "reason": "No JSON payload provided"
        }), 400

    result = sc.run(data)
    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "name": "Supreme Computation",
        "status": "ACTIVE",
        "message": "Universal invariant evaluation interface online"
    })

if __name__ == "__main__":
    app.run(debug=True)
