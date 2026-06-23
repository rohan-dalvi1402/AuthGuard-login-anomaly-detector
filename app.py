from flask import Flask, request, jsonify
from detector import log_attempt

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    data = request.json

    username = data.get("username")
    password = data.get("password")

    # Fake auth logic
    if username == "admin" and password == "password123":
        success = True
    else:
        success = False

    attack = log_attempt(ip, success)

    if attack:
        return jsonify({"alert": "Brute-force detected"}), 403

    return jsonify({"success": success})

if __name__ == "__main__":
    app.run(debug=True)
