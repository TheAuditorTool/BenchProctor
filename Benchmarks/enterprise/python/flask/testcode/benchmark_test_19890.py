# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest19890(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
