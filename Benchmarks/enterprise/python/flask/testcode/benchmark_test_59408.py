# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def BenchmarkTest59408():
    raw_body = request.get_data(as_text=True)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return jsonify({'error': 'forbidden'}), 400
    processed = raw_body
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
