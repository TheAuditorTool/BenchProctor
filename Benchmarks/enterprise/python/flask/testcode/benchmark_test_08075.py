# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest08075():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
