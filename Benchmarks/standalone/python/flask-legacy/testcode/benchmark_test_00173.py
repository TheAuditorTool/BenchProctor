# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Flask, request, jsonify
import json


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00173", methods=["POST"])
def BenchmarkTest00173():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
