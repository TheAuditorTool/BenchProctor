# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28664():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
