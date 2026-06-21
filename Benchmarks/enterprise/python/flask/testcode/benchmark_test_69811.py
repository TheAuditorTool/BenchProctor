# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest69811(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
