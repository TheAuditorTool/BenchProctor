# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69834():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
