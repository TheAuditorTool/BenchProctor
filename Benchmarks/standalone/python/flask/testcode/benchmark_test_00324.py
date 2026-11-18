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


@app.route("/BenchmarkTest00324", methods=["POST"])
def BenchmarkTest00324():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    parsed = json.loads(data)
    return jsonify({'parsed': str(parsed)}), 200
