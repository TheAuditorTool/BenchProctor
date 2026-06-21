# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08285():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    return jsonify({'error': 'An internal error occurred'}), 500
