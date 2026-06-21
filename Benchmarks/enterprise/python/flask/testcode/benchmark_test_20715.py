# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20715():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
