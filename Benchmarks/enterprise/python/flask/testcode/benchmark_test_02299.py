# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02299():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
