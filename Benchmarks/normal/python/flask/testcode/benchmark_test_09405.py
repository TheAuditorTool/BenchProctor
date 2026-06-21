# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest09405():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return jsonify({"result": "success"})
