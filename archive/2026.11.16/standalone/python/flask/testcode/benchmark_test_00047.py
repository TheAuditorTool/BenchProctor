# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import subprocess


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00047", methods=["POST"])
def BenchmarkTest00047():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
