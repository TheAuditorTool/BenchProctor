# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest37289(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
