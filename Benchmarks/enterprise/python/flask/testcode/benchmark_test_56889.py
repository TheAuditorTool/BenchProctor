# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56889():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
