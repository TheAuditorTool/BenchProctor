# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def BenchmarkTest34226():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
