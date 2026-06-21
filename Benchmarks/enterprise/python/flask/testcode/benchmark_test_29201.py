# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest29201(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
