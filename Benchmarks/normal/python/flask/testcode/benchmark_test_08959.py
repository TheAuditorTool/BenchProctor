# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest08959():
    field_value = request.form.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
