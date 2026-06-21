# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18034():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
