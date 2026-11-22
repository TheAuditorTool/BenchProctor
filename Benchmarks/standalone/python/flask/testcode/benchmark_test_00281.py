# SPDX-License-Identifier: Apache-2.0
import json
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00281", methods=["POST"])
def BenchmarkTest00281():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    parsed = json.JSONDecoder().decode(str(data))
    return jsonify({'parsed': str(parsed)}), 200
