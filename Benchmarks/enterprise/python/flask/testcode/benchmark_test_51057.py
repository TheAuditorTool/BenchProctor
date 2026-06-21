# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest51057(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
