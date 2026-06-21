# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22745():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
