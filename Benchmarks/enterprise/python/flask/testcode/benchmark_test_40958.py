# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest40958(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
