# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45281():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return jsonify({"result": "success"})
