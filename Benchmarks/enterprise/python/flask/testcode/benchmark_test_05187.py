# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest05187():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
