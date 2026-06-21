# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def BenchmarkTest42274(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
