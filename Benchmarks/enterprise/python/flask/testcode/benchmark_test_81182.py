# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest81182(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
