# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48422():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
