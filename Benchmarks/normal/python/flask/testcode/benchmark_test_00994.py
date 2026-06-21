# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest00994(path_param):
    path_value = path_param
    data = unquote(path_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
