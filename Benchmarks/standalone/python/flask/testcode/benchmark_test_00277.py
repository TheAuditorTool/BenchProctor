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


@app.route("/BenchmarkTest00277", methods=["POST"])
def BenchmarkTest00277():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
