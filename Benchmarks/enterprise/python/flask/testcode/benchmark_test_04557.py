# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest04557(path_param):
    path_value = path_param
    data = f'{path_value}'
    int(str(data))
    return jsonify({"result": "success"})
