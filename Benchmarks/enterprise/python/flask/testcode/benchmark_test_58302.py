# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58302():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
