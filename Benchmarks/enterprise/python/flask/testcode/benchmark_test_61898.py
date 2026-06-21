# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest61898(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    eval(str(data))
    return jsonify({"result": "success"})
