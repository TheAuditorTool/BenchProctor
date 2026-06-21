# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest19985(path_param):
    path_value = path_param
    data = f'{path_value}'
    requests.get(str(data))
    return jsonify({"result": "success"})
