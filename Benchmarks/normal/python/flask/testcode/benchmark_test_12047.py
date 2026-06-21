# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def BenchmarkTest12047():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
