# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45467():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    int(str(data))
    return jsonify({"result": "success"})
