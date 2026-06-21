# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05264():
    auth_header = request.headers.get('Authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
