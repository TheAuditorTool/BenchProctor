# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest02557():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
