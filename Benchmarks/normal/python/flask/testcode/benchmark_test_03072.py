# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03072():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
