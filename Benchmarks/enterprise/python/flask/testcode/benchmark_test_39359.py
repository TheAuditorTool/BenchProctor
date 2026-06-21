# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest39359():
    user_id = request.args.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
