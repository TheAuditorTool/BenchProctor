# SPDX-License-Identifier: Apache-2.0
import random
import json
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


@app.route("/BenchmarkTest00145", methods=["POST"])
def BenchmarkTest00145():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
