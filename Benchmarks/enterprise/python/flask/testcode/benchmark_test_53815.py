# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest53815(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
