# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19673():
    upload_name = request.files['upload'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return jsonify({"result": "success"})
