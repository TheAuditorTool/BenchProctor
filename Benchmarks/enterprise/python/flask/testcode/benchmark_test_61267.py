# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61267():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    int(str(data))
    return jsonify({"result": "success"})
