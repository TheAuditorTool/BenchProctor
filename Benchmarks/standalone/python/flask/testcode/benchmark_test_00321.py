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


@app.route("/BenchmarkTest00321", methods=["POST"])
def BenchmarkTest00321():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})
