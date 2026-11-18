# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00023", methods=["POST"])
def BenchmarkTest00023():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    requests.get(str(data))
    return jsonify({"result": "success"})
