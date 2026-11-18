# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import defusedxml.ElementTree


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00072", methods=["POST"])
def BenchmarkTest00072():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
