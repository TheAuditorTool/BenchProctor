# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75790():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return jsonify({'error': 'An internal error occurred'}), 500
