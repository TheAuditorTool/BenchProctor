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


@app.route("/BenchmarkTest00286", methods=["POST"])
def BenchmarkTest00286():
    cookie_value = request.cookies.get('session_token', '')
    parsed = json.loads(cookie_value)
    return jsonify({'parsed': str(parsed)}), 200
