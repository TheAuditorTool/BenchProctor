# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00270/<path_param>", methods=["POST"])
def BenchmarkTest00270(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
