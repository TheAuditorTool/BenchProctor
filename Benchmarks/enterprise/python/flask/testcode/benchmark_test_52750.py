# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52750():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    return jsonify({'error': str(forwarded_ip), 'stack': repr(locals())}), 500
