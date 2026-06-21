# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29036():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
