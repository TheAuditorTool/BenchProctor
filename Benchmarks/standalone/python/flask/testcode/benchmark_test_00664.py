# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00664", methods=["POST"])
def BenchmarkTest00664():
    env_value = os.environ.get('APP_INPUT', '')
    data = env_value if env_value else 'default'
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
