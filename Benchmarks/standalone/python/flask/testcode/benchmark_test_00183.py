# SPDX-License-Identifier: Apache-2.0
import json
from urllib.parse import unquote
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00183/<path_param>", methods=["POST"])
def BenchmarkTest00183(path_param):
    path_value = path_param
    data = unquote(path_value)
    parsed = json.loads(data)
    return jsonify({'parsed': str(parsed)}), 200
