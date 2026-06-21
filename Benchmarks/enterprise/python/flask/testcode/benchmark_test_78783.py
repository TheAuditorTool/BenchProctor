# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest78783():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
