# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73220():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
