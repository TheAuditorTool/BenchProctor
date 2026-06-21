# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37268():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
