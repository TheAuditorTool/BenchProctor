# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77620():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
