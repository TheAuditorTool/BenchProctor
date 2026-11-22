# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import ctypes


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00139", methods=["POST"])
def BenchmarkTest00139():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
