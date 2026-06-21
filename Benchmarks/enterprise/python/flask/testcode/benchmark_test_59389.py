# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59389():
    header_value = request.headers.get('X-Custom-Header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
