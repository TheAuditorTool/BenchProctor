# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06876():
    user_id = request.args.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
