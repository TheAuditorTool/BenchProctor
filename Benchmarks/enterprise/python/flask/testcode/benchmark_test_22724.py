# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22724():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
