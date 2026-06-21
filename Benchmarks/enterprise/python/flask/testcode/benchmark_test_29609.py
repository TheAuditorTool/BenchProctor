# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest29609():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    def _primary():
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
