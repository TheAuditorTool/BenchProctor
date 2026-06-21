# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest19637(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
