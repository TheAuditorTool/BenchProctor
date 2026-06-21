# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest06031():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
