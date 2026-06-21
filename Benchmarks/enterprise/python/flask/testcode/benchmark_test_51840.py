# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
import json


def BenchmarkTest51840(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
