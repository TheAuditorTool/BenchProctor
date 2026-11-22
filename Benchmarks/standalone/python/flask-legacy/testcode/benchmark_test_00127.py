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


@app.route("/BenchmarkTest00127", methods=["POST"])
def BenchmarkTest00127():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ' '.join(parts)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
