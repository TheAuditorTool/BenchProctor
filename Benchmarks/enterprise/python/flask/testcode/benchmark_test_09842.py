# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09842():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
