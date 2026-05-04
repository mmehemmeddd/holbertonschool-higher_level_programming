from flask import Flask, jsonify, request

app = Flask(__name__)

# Boş users lüğəti (checker üçün test data olmamalıdır)
users = {}


# ── 1. KÖK ENDPOİNT ─────────────────────────────────────────
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# ── 2. DATA ENDPOİNTİ — bütün istifadəçi adları ─────────────
@app.route("/data")
def data():
    return jsonify(list(users.keys()))


# ── 3. STATUS ENDPOİNTİ ──────────────────────────────────────
@app.route("/status")
def status():
    return "OK"


# ── 4. DİNAMİK ROUTE — tək istifadəçi ───────────────────────
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


# ── 5. POST — yeni istifadəçi əlavə et ───────────────────────
@app.route("/add_user", methods=["POST"])
def add_user():
    # JSON deyilsə → 400
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # username yoxdursa → 400
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # username artıq varsa → 409
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini əlavə et
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
