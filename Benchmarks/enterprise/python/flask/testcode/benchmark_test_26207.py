# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26207():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
