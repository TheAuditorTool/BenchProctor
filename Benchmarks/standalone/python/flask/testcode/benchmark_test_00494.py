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


@app.route("/BenchmarkTest00494", methods=["POST"])
def BenchmarkTest00494():
    auth_header = request.headers.get('Authorization', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(auth_header))
    os.unlink(checked_path)
    return jsonify({"result": "success"})
