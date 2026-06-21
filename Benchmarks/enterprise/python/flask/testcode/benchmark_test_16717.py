# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16717():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
