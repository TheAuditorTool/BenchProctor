# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16028():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    return jsonify({'error': 'An internal error occurred'}), 500
