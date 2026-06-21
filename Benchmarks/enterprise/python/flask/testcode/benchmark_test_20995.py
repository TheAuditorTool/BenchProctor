# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest20995():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
