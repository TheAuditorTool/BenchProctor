# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00646", methods=["POST"])
def BenchmarkTest00646():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    eval(str(data))
    return jsonify({"result": "success"})
