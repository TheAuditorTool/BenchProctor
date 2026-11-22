# SPDX-License-Identifier: Apache-2.0
import ldap3
from dataclasses import dataclass
from flask import Flask, request, jsonify
import os


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00181", methods=["POST"])
def BenchmarkTest00181():
    raw_body = request.get_data(as_text=True)
    form = FormData(payload=raw_body)
    data = form.payload
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return jsonify({"result": "success"})
