# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74131():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
