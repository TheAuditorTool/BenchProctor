# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05614():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
