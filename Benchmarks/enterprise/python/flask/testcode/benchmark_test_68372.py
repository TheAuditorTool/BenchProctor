# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest68372():
    user_id = request.args.get('id', '')
    data = to_text(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
