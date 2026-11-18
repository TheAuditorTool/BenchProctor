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


@app.route("/BenchmarkTest00582", methods=["POST"])
def BenchmarkTest00582():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
