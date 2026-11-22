# SPDX-License-Identifier: Apache-2.0
from Crypto.Hash import SHA256
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00149", methods=["POST"])
def BenchmarkTest00149():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    digest = SHA256.new(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
