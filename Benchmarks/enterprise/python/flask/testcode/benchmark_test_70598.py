# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70598():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = json_value
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
