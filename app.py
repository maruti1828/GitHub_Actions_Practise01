from flask import Flask, jsonify, request

app = Flask(__name__)


def add_numbers(a: int, b: int) -> int:
    return a + b


@app.route("/")
def home():
    return jsonify({"status": "running", "message": "Hello, GitHub Actions!"})


@app.route("/add")
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return jsonify({"error": "Inputs must be integers"}), 400

    return jsonify({"result": add_numbers(a, b)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
