# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00071", methods=["POST"])
def BenchmarkTest00071():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return jsonify({"result": "success"})
