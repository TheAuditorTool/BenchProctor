# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest75306(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    eval(str(data))
    return jsonify({"result": "success"})
