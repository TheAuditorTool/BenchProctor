# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest06366(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
