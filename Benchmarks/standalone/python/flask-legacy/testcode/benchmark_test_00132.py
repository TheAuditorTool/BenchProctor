# SPDX-License-Identifier: Apache-2.0
import ldap3
from flask import Flask, request, jsonify
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


@app.route("/BenchmarkTest00132", methods=["POST"])
def BenchmarkTest00132():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.#%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return jsonify({"result": "success"})
