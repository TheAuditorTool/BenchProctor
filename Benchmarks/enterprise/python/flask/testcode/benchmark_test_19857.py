# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19857():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
