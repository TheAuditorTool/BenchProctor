# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest74516(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
