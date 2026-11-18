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


@app.route("/BenchmarkTest00450", methods=["POST"])
def BenchmarkTest00450():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ' '.join(parts)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return jsonify({"result": "success"})
