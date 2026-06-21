# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06741():
    host_value = request.headers.get('Host', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
