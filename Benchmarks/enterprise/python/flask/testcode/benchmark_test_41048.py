# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest41048():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
