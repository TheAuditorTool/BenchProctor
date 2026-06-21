# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77901():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
