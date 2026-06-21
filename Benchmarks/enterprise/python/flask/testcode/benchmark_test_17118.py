# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest17118():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    requests.get(str(data))
    return jsonify({"result": "success"})
