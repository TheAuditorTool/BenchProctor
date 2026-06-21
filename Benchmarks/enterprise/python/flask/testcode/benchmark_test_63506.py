# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63506():
    auth_header = request.headers.get('Authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
