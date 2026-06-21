# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44473():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
