# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest06224():
    origin_value = request.headers.get('Origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
