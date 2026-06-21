# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06453():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
