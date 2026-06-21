# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest63770(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
