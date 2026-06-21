# SPDX-License-Identifier: Apache-2.0
import ldap
import re
import os
from flask import jsonify


def BenchmarkTest25155():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
