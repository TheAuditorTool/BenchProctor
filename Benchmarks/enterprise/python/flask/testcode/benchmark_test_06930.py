# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06930():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
