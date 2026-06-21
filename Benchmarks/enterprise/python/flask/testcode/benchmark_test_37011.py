# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37011():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
