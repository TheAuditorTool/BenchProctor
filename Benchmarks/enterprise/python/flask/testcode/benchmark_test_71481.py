# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest71481():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(json_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = json_value
    values = str(processed).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
