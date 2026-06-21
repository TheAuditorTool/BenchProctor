# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23395():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
