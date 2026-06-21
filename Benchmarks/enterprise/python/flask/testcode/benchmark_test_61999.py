# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest61999(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    eval(str(data))
    return jsonify({"result": "success"})
