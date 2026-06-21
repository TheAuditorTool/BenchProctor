# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest05993(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
