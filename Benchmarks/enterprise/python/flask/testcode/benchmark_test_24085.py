# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest24085(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
