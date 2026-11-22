# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00339", methods=["POST"])
def BenchmarkTest00339():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
