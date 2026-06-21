# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03183():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
