# SPDX-License-Identifier: Apache-2.0
import ctypes
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00311", methods=["POST"])
def BenchmarkTest00311():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value!s}'
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return jsonify({'allocated': len(records)}), 200
