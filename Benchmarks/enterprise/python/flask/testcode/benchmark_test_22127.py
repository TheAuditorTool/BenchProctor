# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest22127():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
