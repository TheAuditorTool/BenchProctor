# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest30105():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not auth_check(session.get('user', ''), str(json_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
