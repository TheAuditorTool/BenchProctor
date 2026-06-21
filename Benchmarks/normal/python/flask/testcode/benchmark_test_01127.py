# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest01127(path_param):
    path_value = path_param
    if str(path_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
