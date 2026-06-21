# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest48038(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    eval(str(data))
    return jsonify({"result": "success"})
