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


@app.route("/BenchmarkTest00315", methods=["POST"])
def BenchmarkTest00315():
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
