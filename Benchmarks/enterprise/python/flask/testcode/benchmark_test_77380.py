# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77380():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    return jsonify({'error': 'An internal error occurred'}), 500
