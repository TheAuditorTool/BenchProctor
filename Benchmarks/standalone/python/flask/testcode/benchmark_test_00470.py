# SPDX-License-Identifier: Apache-2.0
import yaml
from urllib.parse import unquote
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00470", methods=["POST"])
def BenchmarkTest00470():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
