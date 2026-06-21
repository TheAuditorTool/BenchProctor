# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50584():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
