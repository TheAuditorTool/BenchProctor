# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00275", methods=["POST"])
def BenchmarkTest00275():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    requests.get(str(data))
    return jsonify({"result": "success"})
