# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05789():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    return jsonify({'error': 'An internal error occurred'}), 500
