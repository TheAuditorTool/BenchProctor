# SPDX-License-Identifier: Apache-2.0
import base64
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


@app.route("/BenchmarkTest00215", methods=["POST"])
def BenchmarkTest00215():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
