from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify(ok=True, message="Hello from Flask")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
