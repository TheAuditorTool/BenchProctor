# SPDX-License-Identifier: Apache-2.0
import ldap
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest76105():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
