# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06258():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
