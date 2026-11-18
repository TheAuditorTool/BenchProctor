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


@app.route("/BenchmarkTest00111", methods=["POST"])
def BenchmarkTest00111():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    os.unlink(checked_path)
    return jsonify({"result": "success"})
