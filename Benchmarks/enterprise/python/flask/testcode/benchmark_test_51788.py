# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51788():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
