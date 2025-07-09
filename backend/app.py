from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

@app.route("/contact", methods=["POST", "OPTIONS"])
def contact():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    print(f"Received message from {name} ({email}): {message}")

    return jsonify({"success": True}), 200

if __name__ == "__main__":
    app.run(debug=True)