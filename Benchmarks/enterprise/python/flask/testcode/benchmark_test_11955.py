# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest11955(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
