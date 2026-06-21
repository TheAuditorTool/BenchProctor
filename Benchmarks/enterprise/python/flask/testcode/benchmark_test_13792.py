# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest13792(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
