# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65698():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    return jsonify({'error': 'An internal error occurred'}), 500
