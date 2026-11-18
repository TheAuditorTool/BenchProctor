# SPDX-License-Identifier: Apache-2.0
import os
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


@app.route("/BenchmarkTest00069", methods=["POST"])
def BenchmarkTest00069():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = RequestPayload(profile_value).value
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
