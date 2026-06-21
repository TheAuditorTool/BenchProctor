# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest08117():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
