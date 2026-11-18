# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import request, jsonify
from marshmallow import Schema, fields, validate, ValidationError


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00104", methods=["POST"])
def BenchmarkTest00104():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
