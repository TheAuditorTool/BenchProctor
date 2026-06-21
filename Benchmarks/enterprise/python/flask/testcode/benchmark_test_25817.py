# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25817():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
