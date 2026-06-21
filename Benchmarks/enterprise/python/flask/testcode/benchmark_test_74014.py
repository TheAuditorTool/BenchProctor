# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74014():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
