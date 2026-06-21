# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json


def BenchmarkTest66460(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
