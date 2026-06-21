# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest56038():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
