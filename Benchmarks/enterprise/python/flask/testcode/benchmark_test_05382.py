# SPDX-License-Identifier: Apache-2.0
import ldap
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest05382():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
