# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01421():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = default_blank(json_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
