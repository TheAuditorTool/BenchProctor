# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest77516():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
