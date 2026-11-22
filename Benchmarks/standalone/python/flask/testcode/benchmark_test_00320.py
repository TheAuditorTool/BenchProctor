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


@app.route("/BenchmarkTest00320", methods=["POST"])
def BenchmarkTest00320():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    return render_template_string('<div>{{ value|safe }}</div>', value=str(data))
