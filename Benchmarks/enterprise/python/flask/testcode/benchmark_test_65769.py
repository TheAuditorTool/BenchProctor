# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest65769(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
