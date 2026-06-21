# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest33558(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
