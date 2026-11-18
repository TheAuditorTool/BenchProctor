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


@app.route("/BenchmarkTest00605", methods=["POST"])
def BenchmarkTest00605():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
