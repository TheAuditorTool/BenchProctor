# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81207():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
