# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37194():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
