# SPDX-License-Identifier: Apache-2.0
import random
from flask import Flask, request, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00254", methods=["POST"])
def BenchmarkTest00254():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
