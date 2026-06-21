# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest53488():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
