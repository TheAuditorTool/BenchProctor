# SPDX-License-Identifier: Apache-2.0
import ldap
import os
from flask import jsonify


def BenchmarkTest19683():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
