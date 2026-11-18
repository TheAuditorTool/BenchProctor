# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00496", methods=["POST"])
def BenchmarkTest00496():
    env_value = os.environ.get('APP_INPUT', '')
    data = ' '.join(str(env_value).split())
    exec(str(data))
    return jsonify({"result": "success"})
