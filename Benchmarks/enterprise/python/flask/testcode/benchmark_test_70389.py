# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest70389():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    os.remove(str(data))
    return jsonify({"result": "success"})
