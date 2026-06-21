# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37937():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    if str(data).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
