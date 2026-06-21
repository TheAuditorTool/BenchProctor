# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38856():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
