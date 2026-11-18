# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00591", methods=["POST"])
def BenchmarkTest00591():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
