# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest21816(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
