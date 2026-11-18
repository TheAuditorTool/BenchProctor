# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00155", methods=["POST"])
def BenchmarkTest00155():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ' '.join(parts)
    return '<div>' + str(data) + '</div>'
