# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59449():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
