# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40847():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
