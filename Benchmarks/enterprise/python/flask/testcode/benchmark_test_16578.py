# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def BenchmarkTest16578(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
