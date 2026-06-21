# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest23675(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
