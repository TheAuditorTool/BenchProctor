# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest73937(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    eval(str(data))
    return jsonify({"result": "success"})
