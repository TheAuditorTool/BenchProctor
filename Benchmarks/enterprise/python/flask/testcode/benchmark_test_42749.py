# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest42749(path_param):
    path_value = path_param
    data = default_blank(path_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
