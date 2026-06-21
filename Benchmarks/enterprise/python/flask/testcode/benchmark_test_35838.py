# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest35838():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
