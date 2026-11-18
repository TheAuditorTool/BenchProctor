# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db


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
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})
