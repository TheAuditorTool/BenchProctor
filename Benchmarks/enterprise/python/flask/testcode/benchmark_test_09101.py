# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest09101():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = json_value
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
