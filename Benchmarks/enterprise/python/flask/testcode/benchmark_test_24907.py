# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest24907(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
