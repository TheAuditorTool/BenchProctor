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


@app.route("/BenchmarkTest00102", methods=["POST"])
def BenchmarkTest00102():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ' '.join(parts)
    requests.get(str(data))
    return jsonify({"result": "success"})
