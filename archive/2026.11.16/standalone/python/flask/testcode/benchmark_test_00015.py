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


@app.route("/BenchmarkTest00015", methods=["POST"])
def BenchmarkTest00015():
    env_value = os.environ.get('APP_INPUT', '')
    subprocess.run('echo ' + str(env_value), shell=True)
    return jsonify({"result": "success"})
