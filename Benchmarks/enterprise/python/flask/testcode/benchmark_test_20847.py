# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20847():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    eval(str(json_value))
    return jsonify({"result": "success"})
