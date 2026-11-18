# SPDX-License-Identifier: Apache-2.0
import bleach
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00701/<path_param>", methods=["POST"])
def BenchmarkTest00701(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    processed = bleach.clean(data)
    return '<div>' + str(processed) + '</div>'
