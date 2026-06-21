# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19406():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
