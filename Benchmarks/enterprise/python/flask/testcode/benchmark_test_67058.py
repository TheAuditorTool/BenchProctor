# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify


def BenchmarkTest67058(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    json.loads(data)
    return jsonify({"result": "success"})
