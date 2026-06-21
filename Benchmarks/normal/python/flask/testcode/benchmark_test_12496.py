# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def BenchmarkTest12496():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(forwarded_ip))
    return jsonify({"result": "success"})
