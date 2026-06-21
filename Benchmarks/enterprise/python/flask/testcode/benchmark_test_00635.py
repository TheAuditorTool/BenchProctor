# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00635():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
