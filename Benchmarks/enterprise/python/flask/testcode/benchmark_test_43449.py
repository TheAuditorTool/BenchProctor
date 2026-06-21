# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest43449(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    requests.get(str(data))
    return jsonify({"result": "success"})
