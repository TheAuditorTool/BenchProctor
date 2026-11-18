# SPDX-License-Identifier: Apache-2.0
import ldap
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


@app.route("/BenchmarkTest00340", methods=["POST"])
def BenchmarkTest00340():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return jsonify({"result": "success"})
