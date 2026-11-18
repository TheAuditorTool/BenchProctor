# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import Flask, request, jsonify
import os
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00453", methods=["POST"])
def BenchmarkTest00453():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return jsonify({"result": "success"})
