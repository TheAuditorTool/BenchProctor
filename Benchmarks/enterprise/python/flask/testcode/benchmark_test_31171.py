# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31171():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
