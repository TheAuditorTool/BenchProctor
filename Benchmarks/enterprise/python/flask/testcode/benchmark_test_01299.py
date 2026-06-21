# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest01299():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    processed = data[:64]
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
