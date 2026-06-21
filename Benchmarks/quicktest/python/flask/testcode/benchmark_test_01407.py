# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01407():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
