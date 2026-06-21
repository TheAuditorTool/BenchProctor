# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest18573():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
