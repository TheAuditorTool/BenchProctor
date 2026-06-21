# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest12585(path_param):
    path_value = path_param
    data = f'{path_value}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
