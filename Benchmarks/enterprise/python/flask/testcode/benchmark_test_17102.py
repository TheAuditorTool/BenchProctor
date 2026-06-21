# SPDX-License-Identifier: Apache-2.0
import ldap
from flask import request, jsonify
import os
import ast


def BenchmarkTest17102():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return jsonify({"result": "success"})
