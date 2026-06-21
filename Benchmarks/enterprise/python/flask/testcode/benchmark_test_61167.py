# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest61167():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
