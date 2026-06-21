# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json


def BenchmarkTest17004(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
