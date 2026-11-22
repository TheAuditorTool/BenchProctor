# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import defusedxml.ElementTree
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00348", methods=["POST"])
def BenchmarkTest00348():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    defusedxml.ElementTree.fromstring(str(db_value))
    return jsonify({"result": "success"})
