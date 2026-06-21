# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73668():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
