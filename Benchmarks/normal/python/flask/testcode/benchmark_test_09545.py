# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09545():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
