import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team A: Campus Helpdesk RAG", stack="flask")

@app.route("/api/ingest", methods=["POST"])
def ep_0(**kwargs):
    # TODO: Upload a document, chunk + embed it
    return jsonify(error="Not implemented", todo="Upload a document, chunk + embed it"), 501

@app.route("/api/ask", methods=["POST"])
def ep_1(**kwargs):
    # TODO: Body: {question} -> {answer, sources[]}
    return jsonify(error="Not implemented", todo="Body: {question} -> {answer, sources[]}"), 501

@app.route("/api/docs", methods=["GET"])
def ep_2(**kwargs):
    # TODO: List ingested documents
    return jsonify(error="Not implemented", todo="List ingested documents"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
