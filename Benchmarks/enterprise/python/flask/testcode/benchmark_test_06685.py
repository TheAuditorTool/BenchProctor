# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06685():
    auth_header = request.headers.get('Authorization', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(auth_header)}
