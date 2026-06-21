# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def BenchmarkTest63367(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
