# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60540():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
