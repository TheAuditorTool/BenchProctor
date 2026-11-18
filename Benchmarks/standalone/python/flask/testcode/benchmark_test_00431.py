# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import socket


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00431", methods=["POST"])
def BenchmarkTest00431():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
