# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest07404(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    requests.get(str(data))
    return jsonify({"result": "success"})
