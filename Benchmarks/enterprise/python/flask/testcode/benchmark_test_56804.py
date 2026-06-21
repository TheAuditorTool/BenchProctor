# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest56804():
    user_id = request.args.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    os.seteuid(65534)
    return jsonify({"result": "success"})
