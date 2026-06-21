# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def BenchmarkTest23682():
    multipart_value = request.form.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(multipart_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = multipart_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
