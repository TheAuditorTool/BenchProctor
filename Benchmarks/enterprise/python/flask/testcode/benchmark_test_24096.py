# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24096():
    ua_value = request.headers.get('User-Agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
