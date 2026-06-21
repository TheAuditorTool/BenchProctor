# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest20251(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
