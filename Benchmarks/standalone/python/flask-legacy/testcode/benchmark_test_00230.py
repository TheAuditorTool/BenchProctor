# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import Flask, jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00230", methods=["POST"])
def BenchmarkTest00230():
    env_value = os.environ.get('APP_INPUT', '')
    data = ' '.join(str(env_value).split())
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
