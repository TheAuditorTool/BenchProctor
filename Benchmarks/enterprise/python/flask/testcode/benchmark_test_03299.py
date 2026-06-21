# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def BenchmarkTest03299():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
