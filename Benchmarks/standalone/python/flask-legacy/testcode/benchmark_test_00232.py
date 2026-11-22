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


@app.route("/BenchmarkTest00232", methods=["POST"])
def BenchmarkTest00232():
    field_value = request.form.get('field', '')
    digest = SHA256.new(str(field_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
