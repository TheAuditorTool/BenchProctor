# SPDX-License-Identifier: Apache-2.0
import yaml
import base64
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00090", methods=["POST"])
def BenchmarkTest00090():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
