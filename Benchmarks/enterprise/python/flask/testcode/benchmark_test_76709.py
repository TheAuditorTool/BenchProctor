# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76709():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
