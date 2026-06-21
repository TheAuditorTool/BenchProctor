# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14176():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
