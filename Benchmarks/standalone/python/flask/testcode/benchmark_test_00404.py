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


@app.route("/BenchmarkTest00404", methods=["POST"])
def BenchmarkTest00404():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return jsonify({"result": "success"})
