# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36190():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
