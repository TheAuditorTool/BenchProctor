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


@app.route("/BenchmarkTest00072", methods=["POST"])
def BenchmarkTest00072():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
