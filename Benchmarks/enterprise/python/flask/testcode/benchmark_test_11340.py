# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest11340():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
