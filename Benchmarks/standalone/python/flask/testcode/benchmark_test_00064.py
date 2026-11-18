# SPDX-License-Identifier: Apache-2.0
import hashlib
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


@app.route("/BenchmarkTest00064", methods=["POST"])
def BenchmarkTest00064():
    env_value = os.environ.get('APP_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
