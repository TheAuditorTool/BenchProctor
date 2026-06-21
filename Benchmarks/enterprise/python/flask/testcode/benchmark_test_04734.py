# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest04734(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
