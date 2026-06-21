# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81059():
    origin_value = request.headers.get('Origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
