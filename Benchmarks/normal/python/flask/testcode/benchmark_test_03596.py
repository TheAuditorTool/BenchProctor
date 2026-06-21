# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03596():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
