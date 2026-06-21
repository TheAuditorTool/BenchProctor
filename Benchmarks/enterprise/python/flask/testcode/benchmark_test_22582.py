# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22582():
    host_value = request.headers.get('Host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
