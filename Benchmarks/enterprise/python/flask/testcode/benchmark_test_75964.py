# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest75964():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
