# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66284():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    return jsonify({'error': 'An internal error occurred'}), 500
