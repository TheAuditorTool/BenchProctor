# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
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


@app.route("/BenchmarkTest00002", methods=["POST"])
def BenchmarkTest00002():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})
