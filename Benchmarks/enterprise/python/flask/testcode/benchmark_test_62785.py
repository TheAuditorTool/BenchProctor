# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62785():
    host_value = request.headers.get('Host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    eval(str(data))
    return jsonify({"result": "success"})
