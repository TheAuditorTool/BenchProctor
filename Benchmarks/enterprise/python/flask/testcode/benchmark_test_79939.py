# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79939():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    return jsonify({'error': 'An internal error occurred'}), 500
