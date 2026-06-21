# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest47748():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = normalise_input(json_value)
    return jsonify({'error': 'An internal error occurred'}), 500
