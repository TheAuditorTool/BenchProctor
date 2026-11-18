# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify
import ctypes


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00182", methods=["POST"])
def BenchmarkTest00182():
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
