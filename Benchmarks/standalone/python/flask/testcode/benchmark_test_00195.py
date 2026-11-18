# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00195", methods=["POST"])
def BenchmarkTest00195():
    env_value = os.environ.get('APP_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
