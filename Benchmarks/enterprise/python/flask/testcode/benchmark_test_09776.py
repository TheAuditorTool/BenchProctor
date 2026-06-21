# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09776():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    exec(str(data))
    return jsonify({"result": "success"})
