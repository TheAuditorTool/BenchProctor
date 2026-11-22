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


@app.route("/BenchmarkTest00118", methods=["POST"])
def BenchmarkTest00118():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
