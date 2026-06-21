# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest17424():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
