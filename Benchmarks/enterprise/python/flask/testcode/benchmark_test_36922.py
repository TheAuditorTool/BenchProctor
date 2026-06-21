# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36922():
    header_value = request.headers.get('X-Custom-Header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
