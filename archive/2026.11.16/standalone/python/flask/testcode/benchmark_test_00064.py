# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import Flask, jsonify
import os
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00064", methods=["POST"])
def BenchmarkTest00064():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return jsonify({"result": "success"})
