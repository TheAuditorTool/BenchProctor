# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21823():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
