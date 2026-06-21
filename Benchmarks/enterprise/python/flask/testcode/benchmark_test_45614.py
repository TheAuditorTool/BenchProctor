# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest45614(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
