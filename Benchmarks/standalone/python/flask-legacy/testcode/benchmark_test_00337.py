# SPDX-License-Identifier: Apache-2.0
import ldap3
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


@app.route("/BenchmarkTest00337", methods=["POST"])
def BenchmarkTest00337():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return jsonify({"result": "success"})
