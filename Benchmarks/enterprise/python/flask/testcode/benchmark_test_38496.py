# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest38496():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
