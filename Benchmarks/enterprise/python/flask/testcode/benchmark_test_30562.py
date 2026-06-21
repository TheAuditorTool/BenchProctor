# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest30562():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
