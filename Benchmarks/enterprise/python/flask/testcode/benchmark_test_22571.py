# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22571():
    referer_value = request.headers.get('Referer', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
