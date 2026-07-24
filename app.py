from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/prorate", methods=["POST"])
def prorate():
    data = request.get_json()

    # Pull the numbers out of the JSON
    old_price = data["old_price"]
    new_price = data["new_price"]
    days_remaining = data["days_remaining"]
    days_in_actual_month = data["days_in_actual_month"]
    spec = data["spec"]

    difference = new_price - old_price

    if spec == "v1":
        charge = difference * (days_remaining / 30)
    elif spec == "v2":
        charge = difference * (days_remaining / days_in_actual_month)
    else:
        return jsonify({"error": "spec must be v1 or v2"}), 400

    # Return the answer as JSON
    return jsonify({"charge": charge})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)