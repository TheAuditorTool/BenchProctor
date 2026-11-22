# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import request, jsonify


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00048", methods=["POST"])
def BenchmarkTest00048():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ' '.join(parts)
    session.update({'data': str(data)})
    return jsonify({"result": "success"})
