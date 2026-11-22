# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00130", methods=["POST"])
def BenchmarkTest00130():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
