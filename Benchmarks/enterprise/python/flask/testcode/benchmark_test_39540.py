# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39540():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
