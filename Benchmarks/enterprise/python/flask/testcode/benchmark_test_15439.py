# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15439():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
