# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest39044(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
