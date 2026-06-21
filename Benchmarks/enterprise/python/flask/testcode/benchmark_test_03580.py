# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03580():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    int(str(json_value))
    return jsonify({"result": "success"})
