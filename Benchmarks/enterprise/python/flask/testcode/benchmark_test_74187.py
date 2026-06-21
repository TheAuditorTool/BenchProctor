# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74187():
    user_id = request.args.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
