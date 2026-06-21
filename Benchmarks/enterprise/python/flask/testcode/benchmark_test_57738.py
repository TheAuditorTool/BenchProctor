# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest57738():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
