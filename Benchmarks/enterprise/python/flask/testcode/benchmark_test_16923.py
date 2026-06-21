# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16923():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
