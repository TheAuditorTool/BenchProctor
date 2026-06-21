# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest68611(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
