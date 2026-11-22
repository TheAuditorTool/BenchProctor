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


@app.route("/BenchmarkTest00280/<path_param>", methods=["POST"])
def BenchmarkTest00280(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
