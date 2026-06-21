# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61017():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    return jsonify({'error': 'An internal error occurred'}), 500
