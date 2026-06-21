# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest20672():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
