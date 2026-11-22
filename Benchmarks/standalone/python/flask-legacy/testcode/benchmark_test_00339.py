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


@app.route("/BenchmarkTest00339", methods=["POST"])
def BenchmarkTest00339():
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
