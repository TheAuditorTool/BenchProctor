# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest01288():
    user_id = request.args.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
