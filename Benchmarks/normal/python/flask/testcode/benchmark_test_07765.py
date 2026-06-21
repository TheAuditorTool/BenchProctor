# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import jsonify


def BenchmarkTest07765(path_param):
    path_value = path_param
    data = f'{path_value}'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
