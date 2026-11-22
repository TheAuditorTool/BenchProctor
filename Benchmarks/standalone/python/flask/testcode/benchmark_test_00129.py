# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Flask, request, jsonify
import re


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
    if not re.fullmatch("^(asc|desc|name|created)$", str(header_value)):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
