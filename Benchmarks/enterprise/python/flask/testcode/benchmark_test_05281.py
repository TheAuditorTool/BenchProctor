# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05281():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
