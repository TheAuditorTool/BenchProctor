# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00303():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
