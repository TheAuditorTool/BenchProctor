# SPDX-License-Identifier: Apache-2.0
import ldap
import os
from flask import jsonify


def BenchmarkTest34048():
    env_value = os.environ.get('USER_INPUT', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(env_value))
    return jsonify({"result": "success"})
