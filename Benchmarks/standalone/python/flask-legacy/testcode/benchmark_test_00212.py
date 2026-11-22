# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00212", methods=["POST"])
def BenchmarkTest00212():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    value = label.upper()
    return jsonify({'plan': value}), 200
