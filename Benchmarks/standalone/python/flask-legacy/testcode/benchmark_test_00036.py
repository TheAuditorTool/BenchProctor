# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00036", methods=["POST"])
def BenchmarkTest00036():
    upload_name = request.files['upload'].filename
    digest = hashlib.md5(str(upload_name).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
