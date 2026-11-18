# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import json
import ctypes


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00029", methods=["POST"])
def BenchmarkTest00029():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
