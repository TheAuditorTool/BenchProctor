# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68645():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    return jsonify({'error': 'An internal error occurred'}), 500
