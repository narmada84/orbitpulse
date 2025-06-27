from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Narmada Karthika Chitturi on AKS!"

@app.route("/healthz")
def health():
    return "OK", 200

@app.route("/version")
def version():
    return "v1.0", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)