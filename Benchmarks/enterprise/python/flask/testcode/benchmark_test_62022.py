# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62022():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    return jsonify({'error': 'An internal error occurred'}), 500
