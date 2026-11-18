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


@app.route("/BenchmarkTest00081", methods=["POST"])
def BenchmarkTest00081():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    requests.get(str(data))
    return jsonify({"result": "success"})
