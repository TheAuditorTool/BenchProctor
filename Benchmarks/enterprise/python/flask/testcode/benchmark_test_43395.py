# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43395():
    origin_value = request.headers.get('Origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return jsonify({"result": "success"})
