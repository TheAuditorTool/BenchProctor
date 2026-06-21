# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest52741(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
