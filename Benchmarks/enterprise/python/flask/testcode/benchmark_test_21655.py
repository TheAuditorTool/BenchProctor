# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21655():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    return jsonify({'error': 'An internal error occurred'}), 500
