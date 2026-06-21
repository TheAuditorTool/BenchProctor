# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest18606():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        granted = auth_check('resource', str(header_value))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
