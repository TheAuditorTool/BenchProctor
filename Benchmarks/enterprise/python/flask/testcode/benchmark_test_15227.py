# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15227():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
