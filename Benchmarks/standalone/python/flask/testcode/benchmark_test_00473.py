# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00473/<path_param>", methods=["POST"])
def BenchmarkTest00473(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
