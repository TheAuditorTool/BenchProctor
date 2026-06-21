# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56460():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
