# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40618():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
