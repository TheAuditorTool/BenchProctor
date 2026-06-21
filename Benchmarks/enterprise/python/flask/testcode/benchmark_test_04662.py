# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04662():
    origin_value = request.headers.get('Origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
