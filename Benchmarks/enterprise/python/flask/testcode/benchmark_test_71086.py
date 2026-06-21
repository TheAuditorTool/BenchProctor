# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest71086():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    json.loads(json_value)
    return jsonify({"result": "success"})
