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


@app.route("/BenchmarkTest00152", methods=["POST"])
def BenchmarkTest00152():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
