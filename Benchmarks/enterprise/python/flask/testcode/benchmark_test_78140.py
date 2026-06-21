# SPDX-License-Identifier: Apache-2.0
import ldap
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78140():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
