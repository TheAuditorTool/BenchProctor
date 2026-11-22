# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import Flask, request
from flask import render_template_string
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00023", methods=["POST"])
def BenchmarkTest00023():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    return render_template_string('<div>{{ value }}</div>', value=str(data))
