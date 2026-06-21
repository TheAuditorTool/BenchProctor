# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest53152():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    if not re.fullmatch('^[\\w\\s.*]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
