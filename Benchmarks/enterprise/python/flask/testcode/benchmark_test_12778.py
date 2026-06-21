# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest12778(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
