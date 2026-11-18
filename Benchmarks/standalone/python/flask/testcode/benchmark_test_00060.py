# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00060", methods=["POST"])
def BenchmarkTest00060():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return redirect(str(data))
