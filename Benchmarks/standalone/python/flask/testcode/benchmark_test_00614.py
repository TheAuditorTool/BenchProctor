# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import Flask, request, jsonify
import json
import os
from marshmallow import Schema, fields, validate, ValidationError


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00614", methods=["POST"])
def BenchmarkTest00614():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.#%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return jsonify({"result": "success"})
