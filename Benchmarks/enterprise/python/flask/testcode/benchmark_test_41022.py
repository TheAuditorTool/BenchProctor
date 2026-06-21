# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest41022():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
