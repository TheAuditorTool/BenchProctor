# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59310():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
