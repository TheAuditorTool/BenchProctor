# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest13574():
    host_value = request.headers.get('Host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
