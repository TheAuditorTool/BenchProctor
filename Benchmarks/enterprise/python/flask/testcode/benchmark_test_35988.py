# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35988():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
