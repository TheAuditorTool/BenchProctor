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


@app.route("/BenchmarkTest00067", methods=["POST"])
def BenchmarkTest00067():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
