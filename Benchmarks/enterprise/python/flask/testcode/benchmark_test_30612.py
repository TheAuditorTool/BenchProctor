# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest30612(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
