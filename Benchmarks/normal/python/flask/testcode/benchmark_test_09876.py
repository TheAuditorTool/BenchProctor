# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09876():
    user_id = request.args.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    eval(str(data))
    return jsonify({"result": "success"})
