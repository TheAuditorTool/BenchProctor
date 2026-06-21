# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70974():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    return jsonify({'error': 'An internal error occurred'}), 500
