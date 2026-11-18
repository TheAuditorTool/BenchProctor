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


@app.route("/BenchmarkTest00018", methods=["POST"])
def BenchmarkTest00018():
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
