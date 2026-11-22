# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00269", methods=["POST"])
def BenchmarkTest00269():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
