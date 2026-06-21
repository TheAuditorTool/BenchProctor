# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest55075(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
