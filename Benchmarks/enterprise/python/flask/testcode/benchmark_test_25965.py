# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import request, jsonify


def BenchmarkTest25965():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
