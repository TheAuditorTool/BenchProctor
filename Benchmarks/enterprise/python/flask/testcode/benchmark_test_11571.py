# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11571():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
