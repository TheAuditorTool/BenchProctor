# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20006():
    header_value = request.headers.get('X-Custom-Header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
