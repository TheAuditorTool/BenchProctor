# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52033():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
