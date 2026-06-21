# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def BenchmarkTest63305(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
