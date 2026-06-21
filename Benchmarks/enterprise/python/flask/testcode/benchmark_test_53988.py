# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest53988():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
