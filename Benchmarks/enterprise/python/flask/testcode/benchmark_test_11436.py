# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest11436():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
