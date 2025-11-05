from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory database
cases = [
    {"id": 1, "customer_name": "Alice", "case_type": "Loan", "description": "Loan request", "status": "OPEN"},
    {"id": 2, "customer_name": "Bob", "case_type": "Account", "description": "Open new account", "status": "IN_PROGRESS"},
]

def get_next_id() -> int:
    return max((c["id"] for c in cases), default=0) + 1

@app.route("/")
def index():
    return render_template("index.html", cases=cases)

@app.route("/cases", methods=["GET", "POST"])
def manage_cases():
    if request.method == "POST":
        data = request.form if request.form else request.get_json(force=True)
        customer_name = data.get("customer_name", "").strip()
        case_type = data.get("case_type", "").strip()
        description = data.get("description", "").strip()
        if not (customer_name and case_type and description):
            return "Missing data", 400
        new_case = {
            "id": get_next_id(),
            "customer_name": customer_name,
            "case_type": case_type,
            "description": description,
            "status": "OPEN"
        }
        cases.append(new_case)
        return redirect(url_for("index"))
    return jsonify(cases)

@app.route("/cases/<int:case_id>", methods=["PUT", "DELETE"])
def modify_case(case_id: int):
    case = next((c for c in cases if c["id"] == case_id), None)
    if not case:
        return "Case not found", 404
    if request.method == "PUT":
        data = request.form if request.form else request.get_json(force=True)
        case["description"] = data.get("description", case["description"])
        case["status"] = data.get("status", case["status"])
        return redirect(url_for("index"))
    if request.method == "DELETE":
        cases.remove(case)
        return "", 204

@app.route("/cases/<int:case_id>/close", methods=["POST"])
def close_case(case_id: int):
    case = next((c for c in cases if c["id"] == case_id), None)
    if not case:
        return "Case not found", 404
    case["status"] = "CLOSED"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
