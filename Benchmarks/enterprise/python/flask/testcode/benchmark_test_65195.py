# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest65195():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    auth_check('user', data)
    return jsonify({"result": "success"})
