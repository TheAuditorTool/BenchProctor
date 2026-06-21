# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def BenchmarkTest52166():
    raw_body = request.get_data(as_text=True)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(raw_body))
    return jsonify({"result": "success"})
