# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70648():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
