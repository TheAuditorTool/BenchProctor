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


@app.route("/BenchmarkTest00032", methods=["POST"])
def BenchmarkTest00032():
    raw_body = request.get_data(as_text=True)
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
