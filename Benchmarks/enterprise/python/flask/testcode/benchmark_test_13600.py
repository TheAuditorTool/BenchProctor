# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13600():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not str(json_value).isdigit():
        raise ValueError('invalid input: ' + str(json_value))
    return jsonify({"result": "success"})
