# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66188():
    ua_value = request.headers.get('User-Agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
