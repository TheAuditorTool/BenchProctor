# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest16338():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
