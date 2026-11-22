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


@app.route("/BenchmarkTest00012", methods=["POST"])
def BenchmarkTest00012():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    return render_template_string('<div>{{ value }}</div>', value=str(data))
