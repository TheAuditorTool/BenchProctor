# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest00493(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
