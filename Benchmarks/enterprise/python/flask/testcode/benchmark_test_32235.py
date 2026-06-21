# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32235():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
