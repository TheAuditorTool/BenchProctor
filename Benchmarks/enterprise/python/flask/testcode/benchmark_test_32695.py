# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32695():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
