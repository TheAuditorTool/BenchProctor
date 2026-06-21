# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest10219():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
