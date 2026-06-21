# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78500():
    host_value = request.headers.get('Host', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
