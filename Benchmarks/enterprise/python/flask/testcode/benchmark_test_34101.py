# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest34101():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
