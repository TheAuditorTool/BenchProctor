# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest21958(path_param):
    path_value = path_param
    data = relay_value(path_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
