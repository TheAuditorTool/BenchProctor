# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02017():
    raw_body = request.get_data(as_text=True)
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    eval(str(data))
    return jsonify({"result": "success"})
