# SPDX-License-Identifier: Apache-2.0
import ldap
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest56064(path_param):
    path_value = path_param
    data = unquote(path_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
