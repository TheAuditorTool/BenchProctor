# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest77446():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if str(processed) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
