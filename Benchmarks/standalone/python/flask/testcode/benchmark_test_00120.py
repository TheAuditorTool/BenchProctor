# SPDX-License-Identifier: Apache-2.0
import yaml
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


@app.route("/BenchmarkTest00120", methods=["POST"])
def BenchmarkTest00120():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
