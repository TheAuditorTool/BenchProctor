# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56085():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
