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


@app.route("/BenchmarkTest00316", methods=["POST"])
def BenchmarkTest00316():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    parsed = yaml.safe_load(data)
    return jsonify({'parsed': str(parsed)}), 200
