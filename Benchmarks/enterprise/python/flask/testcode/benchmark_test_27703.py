# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest27703(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
