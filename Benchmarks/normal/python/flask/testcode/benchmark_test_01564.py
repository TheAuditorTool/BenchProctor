# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest01564():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(json_value)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
