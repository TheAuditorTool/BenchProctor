# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00021", methods=["POST"])
def BenchmarkTest00021():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return jsonify({"result": "success"})
