# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63655():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
