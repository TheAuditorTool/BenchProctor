# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25496():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
