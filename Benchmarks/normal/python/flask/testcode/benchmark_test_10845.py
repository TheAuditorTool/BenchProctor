# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest10845(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
