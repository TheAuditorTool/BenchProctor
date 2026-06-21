# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08174():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
