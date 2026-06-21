# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26446():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    raise RuntimeError('processing failed: ' + str(json_value))
    return jsonify({"result": "success"})
