# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest55818(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
