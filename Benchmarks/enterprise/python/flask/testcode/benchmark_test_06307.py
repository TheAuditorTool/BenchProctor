# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest06307(path_param):
    path_value = path_param
    data = unquote(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
