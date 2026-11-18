# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import Flask, request, jsonify
import os
from pydantic import Field, ValidationError, create_model


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00429", methods=["POST"])
def BenchmarkTest00429():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.#%\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return jsonify({"result": "success"})
