# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest37537():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
