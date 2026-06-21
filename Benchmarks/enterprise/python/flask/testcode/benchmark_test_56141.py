# SPDX-License-Identifier: Apache-2.0
import ldap
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest56141():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
