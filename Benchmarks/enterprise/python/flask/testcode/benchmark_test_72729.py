# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72729():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
