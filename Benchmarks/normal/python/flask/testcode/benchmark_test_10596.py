# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10596():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
