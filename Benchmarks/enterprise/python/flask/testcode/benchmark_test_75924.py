# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest75924(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
