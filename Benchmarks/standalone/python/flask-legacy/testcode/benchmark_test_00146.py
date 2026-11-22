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


@app.route("/BenchmarkTest00146", methods=["POST"])
def BenchmarkTest00146():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
