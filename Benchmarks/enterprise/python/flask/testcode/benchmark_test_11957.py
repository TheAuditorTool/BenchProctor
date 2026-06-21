# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11957():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
