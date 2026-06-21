# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00268():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
