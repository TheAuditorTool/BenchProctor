# SPDX-License-Identifier: Apache-2.0
from flask import Flask, current_app
from urllib.parse import unquote
from flask import request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00299", methods=["POST"])
def BenchmarkTest00299():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    current_app.config['ACTIVE_TENANT'] = str(data)
    return jsonify({"result": "success"})
