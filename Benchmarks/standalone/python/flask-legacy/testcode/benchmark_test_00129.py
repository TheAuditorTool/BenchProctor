# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import subprocess


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00129", methods=["POST"])
def BenchmarkTest00129():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
