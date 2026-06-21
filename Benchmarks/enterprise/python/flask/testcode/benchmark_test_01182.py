# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest01182(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
