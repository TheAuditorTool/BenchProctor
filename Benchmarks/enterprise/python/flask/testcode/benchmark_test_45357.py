# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45357():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
