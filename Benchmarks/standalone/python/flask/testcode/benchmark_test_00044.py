# SPDX-License-Identifier: Apache-2.0
from Crypto.Hash import MD4
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00044", methods=["POST"])
def BenchmarkTest00044():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    digest = MD4.new(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
