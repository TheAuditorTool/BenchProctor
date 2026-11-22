# SPDX-License-Identifier: Apache-2.0
from flask import Flask, current_app
from flask import jsonify
from marshmallow import Schema, fields, validate, ValidationError
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00035", methods=["POST"])
def BenchmarkTest00035():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    current_app.config['ACTIVE_TENANT'] = str(processed)
    return jsonify({"result": "success"})
