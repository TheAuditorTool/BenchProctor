# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14015():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
