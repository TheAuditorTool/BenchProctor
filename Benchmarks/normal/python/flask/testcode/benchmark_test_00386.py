# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00386():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
