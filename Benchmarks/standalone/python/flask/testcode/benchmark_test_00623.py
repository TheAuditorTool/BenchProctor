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


@app.route("/BenchmarkTest00623", methods=["POST"])
def BenchmarkTest00623():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    requests.get(str(data))
    return jsonify({"result": "success"})
