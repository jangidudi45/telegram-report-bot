# Simple HTTP server for health checks
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "OK", 200

if __name__ == "__main__":
    # Listen on all network interfaces, port 8080
    app.run(host="0.0.0.0", port=8080)
