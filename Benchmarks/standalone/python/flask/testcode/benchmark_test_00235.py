# SPDX-License-Identifier: Apache-2.0
import ctypes
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


@app.route("/BenchmarkTest00235", methods=["POST"])
def BenchmarkTest00235():
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return jsonify({'allocated': len(records)}), 200
