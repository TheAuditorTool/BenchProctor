# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest28634(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
