# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest27451():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
