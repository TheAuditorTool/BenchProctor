# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest55462():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
