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


@app.route("/BenchmarkTest00718", methods=["POST"])
def BenchmarkTest00718():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
