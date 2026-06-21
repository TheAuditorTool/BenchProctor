# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37797():
    multipart_value = request.form.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
