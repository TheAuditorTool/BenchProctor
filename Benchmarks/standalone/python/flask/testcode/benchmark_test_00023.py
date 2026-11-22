# SPDX-License-Identifier: Apache-2.0
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
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(data))
