# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest68526():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
