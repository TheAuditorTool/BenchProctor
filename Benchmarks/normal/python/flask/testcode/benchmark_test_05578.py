# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05578(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.*]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
