# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest68376(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
