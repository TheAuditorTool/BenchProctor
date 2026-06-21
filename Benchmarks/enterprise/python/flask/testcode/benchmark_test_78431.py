# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78431():
    origin_value = request.headers.get('Origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
