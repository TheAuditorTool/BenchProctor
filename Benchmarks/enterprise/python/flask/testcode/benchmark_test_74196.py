# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json


def BenchmarkTest74196(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    os.seteuid(65534)
    return jsonify({"result": "success"})
