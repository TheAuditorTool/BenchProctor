# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00083", methods=["POST"])
def BenchmarkTest00083():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    exec(str(data))
    return jsonify({"result": "success"})
