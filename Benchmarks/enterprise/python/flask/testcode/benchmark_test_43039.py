# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43039():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
