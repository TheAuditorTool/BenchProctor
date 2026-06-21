# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest64631(path_param):
    path_value = path_param
    data = default_blank(path_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
