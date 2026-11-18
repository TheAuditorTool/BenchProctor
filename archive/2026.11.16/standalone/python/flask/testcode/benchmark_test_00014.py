# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00014", methods=["POST"])
def BenchmarkTest00014():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
