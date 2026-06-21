# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest55479():
    upload_name = request.files['upload'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
