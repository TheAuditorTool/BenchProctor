# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest40001():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    auth_check('user', data)
    return jsonify({"result": "success"})
