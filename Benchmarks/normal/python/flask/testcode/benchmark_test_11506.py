# SPDX-License-Identifier: Apache-2.0
import ldap
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest11506():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
