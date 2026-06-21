# SPDX-License-Identifier: Apache-2.0
import ldap
import os
from flask import jsonify


def BenchmarkTest11752():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
