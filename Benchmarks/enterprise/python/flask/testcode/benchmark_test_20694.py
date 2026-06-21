# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest20694():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
