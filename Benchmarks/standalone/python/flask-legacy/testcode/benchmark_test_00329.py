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


@app.route("/BenchmarkTest00329", methods=["POST"])
def BenchmarkTest00329():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return jsonify({"result": "success"})
