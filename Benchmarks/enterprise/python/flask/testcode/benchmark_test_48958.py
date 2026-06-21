# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48958():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
