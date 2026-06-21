# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest72934():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return jsonify({"result": "success"})
