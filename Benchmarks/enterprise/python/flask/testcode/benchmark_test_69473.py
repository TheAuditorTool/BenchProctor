# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69473():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
