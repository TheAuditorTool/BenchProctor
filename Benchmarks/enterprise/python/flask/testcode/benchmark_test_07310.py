# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07310():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
