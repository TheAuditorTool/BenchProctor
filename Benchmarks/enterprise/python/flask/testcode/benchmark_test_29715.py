# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29715():
    header_value = request.headers.get('X-Custom-Header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
