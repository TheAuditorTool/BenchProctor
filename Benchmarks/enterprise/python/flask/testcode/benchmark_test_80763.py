# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest80763():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
