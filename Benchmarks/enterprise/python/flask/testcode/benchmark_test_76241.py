# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def BenchmarkTest76241(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
