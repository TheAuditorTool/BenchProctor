# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64069():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
