from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory "database"
cases = []
case_id_counter = 1

# ---------------------------
# API Endpoints
# ---------------------------

# Create a new case
@app.route("/cases", methods=["POST"])
def create_case():
    global case_id_counter
    data = request.json
    case = {
        "id": case_id_counter,
        "customer_name": data.get("customer_name"),
        "case_type": data.get("case_type"),
        "status": "OPEN",
        "description": data.get("description", "")
    }
    cases.append(case)
    case_id_counter += 1
    return jsonify(case), 201

# List all cases
@app.route("/cases", methods=["GET"])
def list_cases():
    return jsonify(cases)

# Get a single case by ID
@app.route("/cases/<int:case_id>", methods=["GET"])
def get_case(case_id):
    case = next((c for c in cases if c["id"] == case_id), None)
    if not case:
        return jsonify({"error": "Case not found"}), 404
    return jsonify(case)

# Update an existing case
@app.route("/cases/<int:case_id>", methods=["PUT"])
def update_case(case_id):
    data = request.json
    case = next((c for c in cases if c["id"] == case_id), None)
    if not case:
        return jsonify({"error": "Case not found"}), 404
    case["status"] = data.get("status", case["status"])
    case["customer_name"] = data.get("customer_name", case["customer_name"])
    case["case_type"] = data.get("case_type", case["case_type"])
    case["description"] = data.get("description", case["description"])
    return jsonify(case)

# Delete a case
@app.route("/cases/<int:case_id>", methods=["DELETE"])
def delete_case(case_id):
    global cases
    case = next((c for c in cases if c["id"] == case_id), None)
    if not case:
        return jsonify({"error": "Case not found"}), 404
    cases = [c for c in cases if c["id"] != case_id]
    return jsonify({"message": f"Case {case_id} deleted"}), 200

# ---------------------------
# Browser-friendly view
# ---------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", cases=cases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
