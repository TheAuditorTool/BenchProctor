# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49169():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
