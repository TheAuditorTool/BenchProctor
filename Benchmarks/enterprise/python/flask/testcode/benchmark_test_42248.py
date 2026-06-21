# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest42248(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
