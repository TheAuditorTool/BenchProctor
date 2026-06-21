# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35841():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
