# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46438():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
