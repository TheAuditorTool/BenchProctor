# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, jsonify
import os
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))

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
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '{}'.format(api_value)
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(data) + "'")
    return jsonify({"result": "success"})
