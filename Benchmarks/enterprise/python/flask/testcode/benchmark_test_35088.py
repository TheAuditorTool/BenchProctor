# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35088():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(forwarded_ip)}
