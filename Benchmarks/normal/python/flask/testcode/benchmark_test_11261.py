# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest11261():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
