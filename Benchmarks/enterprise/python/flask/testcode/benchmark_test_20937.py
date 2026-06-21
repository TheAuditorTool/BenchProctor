# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20937():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    return jsonify({'error': 'An internal error occurred'}), 500
