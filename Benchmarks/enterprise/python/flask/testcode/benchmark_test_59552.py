# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest59552():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
