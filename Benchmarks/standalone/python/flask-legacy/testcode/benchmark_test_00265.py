# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00265", methods=["POST"])
def BenchmarkTest00265():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
