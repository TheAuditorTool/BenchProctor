# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def BenchmarkTest10879():
    xml_value = request.get_data(as_text=True)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(xml_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = xml_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
