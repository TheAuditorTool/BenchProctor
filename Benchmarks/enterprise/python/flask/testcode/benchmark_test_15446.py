# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15446():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
