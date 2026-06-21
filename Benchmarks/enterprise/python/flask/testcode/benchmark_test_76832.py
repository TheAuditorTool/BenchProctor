# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76832():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
