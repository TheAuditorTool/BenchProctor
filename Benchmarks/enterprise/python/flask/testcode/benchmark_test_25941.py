# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25941():
    ua_value = request.headers.get('User-Agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    return jsonify({'error': 'An internal error occurred'}), 500
