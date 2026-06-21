# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest58130(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
