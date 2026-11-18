# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00548", methods=["POST"])
def BenchmarkTest00548():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return jsonify({"result": "success"})
