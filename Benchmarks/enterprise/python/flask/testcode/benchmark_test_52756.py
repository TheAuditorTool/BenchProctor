# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52756():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    eval(str(data))
    return jsonify({"result": "success"})
