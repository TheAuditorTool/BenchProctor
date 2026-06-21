# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest37535(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
