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


@app.route("/BenchmarkTest00100", methods=["POST"])
def BenchmarkTest00100():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    os.system('echo ' + str(json_value))
    return jsonify({"result": "success"})
