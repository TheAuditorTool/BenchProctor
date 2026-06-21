# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49725():
    origin_value = request.headers.get('Origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
