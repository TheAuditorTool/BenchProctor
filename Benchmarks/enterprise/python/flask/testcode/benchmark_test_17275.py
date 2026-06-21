# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17275():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
