# SPDX-License-Identifier: Apache-2.0
import ldap
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest26815():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
