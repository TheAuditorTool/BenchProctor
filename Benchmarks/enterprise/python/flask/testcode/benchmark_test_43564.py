# SPDX-License-Identifier: Apache-2.0
import ldap
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest43564():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
