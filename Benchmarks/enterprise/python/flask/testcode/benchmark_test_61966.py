# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61966():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
