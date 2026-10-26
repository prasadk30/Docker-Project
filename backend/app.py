from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory list to keep submissions (resets when container restarts)
submissions = []


@app.route("/")
def home():
    return jsonify({"message": "Flask backend is running"})


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    # Basic validation
    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields are required"}), 400

    # Process the data
    entry = {
        "name": name.title(),
        "email": email.lower(),
        "message": message,
        "message_length": len(message),
    }
    submissions.append(entry)

    return jsonify({
        "success": True,
        "reply": f"Hello {entry['name']}! Your message ({entry['message_length']} characters) was received.",
        "total_submissions": len(submissions),
    })


@app.route("/submissions")
def all_submissions():
    return jsonify(submissions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
