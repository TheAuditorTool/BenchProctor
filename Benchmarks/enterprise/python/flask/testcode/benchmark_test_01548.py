# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01548():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
