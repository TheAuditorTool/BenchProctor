# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest78779():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        granted = auth_check('resource', str(forwarded_ip))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
