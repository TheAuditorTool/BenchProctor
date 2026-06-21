# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21280():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
