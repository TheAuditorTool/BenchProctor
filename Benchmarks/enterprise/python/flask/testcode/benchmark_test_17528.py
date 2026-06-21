# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17528():
    auth_header = request.headers.get('Authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    eval(str(data))
    return jsonify({"result": "success"})
