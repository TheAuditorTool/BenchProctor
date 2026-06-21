# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest01829(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
