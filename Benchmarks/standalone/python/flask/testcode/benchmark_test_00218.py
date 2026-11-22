# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00218", methods=["POST"])
def BenchmarkTest00218():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
