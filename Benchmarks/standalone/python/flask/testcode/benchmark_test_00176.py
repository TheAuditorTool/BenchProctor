# SPDX-License-Identifier: Apache-2.0
import ldap3
from flask import Flask, jsonify
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


@app.route("/BenchmarkTest00176/<path_param>", methods=["POST"])
def BenchmarkTest00176(path_param):
    path_value = path_param
    if not re.fullmatch("^(asc|desc|name|created)$", str(path_value)):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return jsonify({"result": "success"})
