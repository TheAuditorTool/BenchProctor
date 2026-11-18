# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import socket


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00118", methods=["POST"])
def BenchmarkTest00118():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
