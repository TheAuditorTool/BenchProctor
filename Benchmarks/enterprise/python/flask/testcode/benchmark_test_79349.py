# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest79349(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
