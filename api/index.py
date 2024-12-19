from flask import Flask, request, jsonify
from api import config

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def handle_all_requests(path):
    return jsonify({"error": config.ERROR_MESSAGE}), config.ERROR_CODE
