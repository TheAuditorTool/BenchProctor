# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00323/<path_param>", methods=["POST"])
def BenchmarkTest00323(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
