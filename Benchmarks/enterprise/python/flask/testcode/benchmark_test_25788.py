# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest25788():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
