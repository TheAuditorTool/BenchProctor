# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest73631():
    multipart_value = request.form.get('multipart_field', '')
    try:
        granted = auth_check('resource', str(multipart_value))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
