# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest41074():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    return jsonify({'error': 'An internal error occurred'}), 500
