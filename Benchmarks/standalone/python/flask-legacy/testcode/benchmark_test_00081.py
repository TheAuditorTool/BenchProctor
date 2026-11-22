# SPDX-License-Identifier: Apache-2.0
from flask import Flask, render_template_string
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00081/<path_param>", methods=["POST"])
def BenchmarkTest00081(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ' '.join(parts)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(data))
