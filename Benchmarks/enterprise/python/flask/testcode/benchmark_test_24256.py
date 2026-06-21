# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24256():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
