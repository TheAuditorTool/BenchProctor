# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00177", methods=["POST"])
def BenchmarkTest00177():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    parsed = yaml.safe_load(data)
    return jsonify({'parsed': str(parsed)}), 200
