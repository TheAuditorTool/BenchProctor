# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import jsonify


def BenchmarkTest43689(path_param):
    path_value = path_param
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(path_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = path_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
