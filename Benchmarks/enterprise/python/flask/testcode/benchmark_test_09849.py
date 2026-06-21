# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest09849(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
