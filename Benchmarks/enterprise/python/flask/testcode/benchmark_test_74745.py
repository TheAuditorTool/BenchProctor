# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74745():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    size = min(int(json_value) if str(json_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
