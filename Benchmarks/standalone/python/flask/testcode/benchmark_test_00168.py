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


@app.route("/BenchmarkTest00168", methods=["POST"])
def BenchmarkTest00168():
    multipart_value = request.form.get('multipart_field', '')
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(multipart_value), token))
    return jsonify({'token': str(token)}), 200
