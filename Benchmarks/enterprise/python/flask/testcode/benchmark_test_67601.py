# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest67601():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
