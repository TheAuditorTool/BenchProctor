# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest09047(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
