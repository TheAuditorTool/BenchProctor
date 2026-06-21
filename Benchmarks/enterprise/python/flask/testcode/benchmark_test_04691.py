# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04691():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
