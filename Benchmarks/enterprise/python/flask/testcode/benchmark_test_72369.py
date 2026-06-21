# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest72369(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
