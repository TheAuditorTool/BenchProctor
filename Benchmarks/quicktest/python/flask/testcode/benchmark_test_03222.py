# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest03222(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
