# SPDX-License-Identifier: Apache-2.0
import ldap
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest72780():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
