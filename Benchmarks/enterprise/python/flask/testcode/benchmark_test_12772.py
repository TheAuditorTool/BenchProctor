# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12772():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
