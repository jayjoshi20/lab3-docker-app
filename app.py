from flask import Flask
app = Flask(__name__)

@app.get("/")
def index():
    return "Hello from Lab 3 via GitHub Actions → ECR (v1)!\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
