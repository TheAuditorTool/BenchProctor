# SPDX-License-Identifier: Apache-2.0
import ldap
import re
import os
from flask import jsonify


def BenchmarkTest07159():
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = env_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
