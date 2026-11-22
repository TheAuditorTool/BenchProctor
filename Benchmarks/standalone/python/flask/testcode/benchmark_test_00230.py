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


@app.route("/BenchmarkTest00230", methods=["POST"])
def BenchmarkTest00230():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
