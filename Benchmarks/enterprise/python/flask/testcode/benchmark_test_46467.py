# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest46467(path_param):
    path_value = path_param
    data = unquote(path_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
