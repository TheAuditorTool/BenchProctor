# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09826():
    user_id = request.args.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
