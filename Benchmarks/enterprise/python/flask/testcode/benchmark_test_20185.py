# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest20185(path_param):
    path_value = path_param
    if str(path_value).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
