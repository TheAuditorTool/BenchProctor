# SPDX-License-Identifier: Apache-2.0
import subprocess
import base64
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00141", methods=["POST"])
def BenchmarkTest00141():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
