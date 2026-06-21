# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest75595(path_param):
    path_value = path_param
    if str(path_value) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
